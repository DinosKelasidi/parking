from abc import ABC, abstractmethod

class ParkingSpotState(ABC):
    """Абстрактный класс состояния парковочного места."""
    
    @abstractmethod
    def reserve(self, parking_spot):
        pass

    @abstractmethod
    def occupy(self, parking_spot):
        pass

    @abstractmethod
    def release(self, parking_spot):
        pass

class FreeState(ParkingSpotState):
    """Состояние 'Свободно'."""
    
    def reserve(self, parking_spot):
        print("Место забронировано.")
        parking_spot.set_state(ReservedState())
    
    def occupy(self, parking_spot):
        print("Место занято.")
        parking_spot.set_state(OccupiedState())
    
    def release(self, parking_spot):
        print("Место уже свободно.")

class ReservedState(ParkingSpotState):
    """Состояние 'Забронировано'."""
    
    def reserve(self, parking_spot):
        print("Место уже забронировано.")
    
    def occupy(self, parking_spot):
        print("Место занято.")
        parking_spot.set_state(OccupiedState())
    
    def release(self, parking_spot):
        print("Бронь отменена, место свободно.")
        parking_spot.set_state(FreeState())

class OccupiedState(ParkingSpotState):
    """Состояние 'Занято'."""
    
    def reserve(self, parking_spot):
        print("Нельзя забронировать занятое место.")
    
    def occupy(self, parking_spot):
        print("Место уже занято.")
    
    def release(self, parking_spot):
        print("Место освобождено.")
        parking_spot.set_state(FreeState())

class ParkingSpot:
    """Класс для парковочного места."""
    
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.state = FreeState()
    
    def set_state(self, state):
        self.state = state
    
    def reserve(self):
        self.state.reserve(self)
    
    def occupy(self):
        self.state.occupy(self)
    
    def release(self):
        self.state.release(self)

class ParkingLot:
    """Класс для управления парковкой."""
    
    def __init__(self, total_spots):
        self.spots = [ParkingSpot(i) for i in range(1, total_spots + 1)]
        self.prices = 10  # Цена за место
    
    def show_available_spots(self):
        available_spots = [spot.spot_id for spot in self.spots if isinstance(spot.state, FreeState)]
        print("Свободные места:", available_spots)
    
    def reserve_spot(self, spot_id):
        if 1 <= spot_id <= len(self.spots):
            self.spots[spot_id - 1].reserve()
        else:
            print("Неверный номер места.")
    
    def occupy_spot(self, spot_id):
        if 1 <= spot_id <= len(self.spots):
            self.spots[spot_id - 1].occupy()
        else:
            print("Неверный номер места.")
    
    def release_spot(self, spot_id):
        if 1 <= spot_id <= len(self.spots):
            self.spots[spot_id - 1].release()
        else:
            print("Неверный номер места.")
    
    def calculate_cost(self, hours):
        return hours * self.prices

if __name__ == "__main__":
    total_spots = int(input("Введите количество парковочных мест: "))
    parking_lot = ParkingLot(total_spots=total_spots)
    
    while True:
        print("\nМеню:")
        print("1. Показать свободные места")
        print("2. Забронировать место")
        print("3. Занять место")
        print("4. Освободить место")
        print("5. Рассчитать стоимость парковки")
        print("6. Выйти")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            parking_lot.show_available_spots()
        
        elif choice == "2":
            spot_id = int(input("Введите номер места для бронирования: "))
            parking_lot.reserve_spot(spot_id)
        
        elif choice == "3":
            spot_id = int(input("Введите номер места для занятия: "))
            parking_lot.occupy_spot(spot_id)
        
        elif choice == "4":
            spot_id = int(input("Введите номер места для освобождения: "))
            parking_lot.release_spot(spot_id)
        
        elif choice == "5":
            hours = int(input("Введите количество часов: "))
            cost = parking_lot.calculate_cost(hours)
            print(f"Стоимость парковки за {hours} час(а): {cost} руб.")
        
        elif choice == "6":
            print("Выход из программы.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")