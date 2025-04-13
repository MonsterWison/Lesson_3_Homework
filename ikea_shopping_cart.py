from ikea_furniture_database_structure import Furniture, engine
from sqlmodel import Session, select

def calculate_total():
    with Session(engine) as session:
        stmt = select(Furniture).where(Furniture.product_id.in_(["W003", "D008", "TV009"]))
        items = session.exec(stmt).all()
        total = sum(item.price for item in items)
        print("購物車商品：")
        for item in items:
            print(f"{item.name} - ${item.price:.2f}")
        print(f"總金額: ${total:.2f}")

if __name__ == "__main__":
    calculate_total()
