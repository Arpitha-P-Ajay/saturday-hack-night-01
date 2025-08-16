


<img width="1920" height="1080" alt="nasahub" src="https://github.com/user-attachments/assets/e8544200-f902-41ee-a2f2-7375cad5043d" />




# Pizza Order API
Simulate a pizza delivery system with endpoints to order, choose toppings, and calculate delivery time. Example: /order?size=medium&toppings=olives,cheese.
Here, users can order pizzas by selecting size and toppings. The backend calculates the price and provides an order summary with estimated delivery time.

## Team member
1. [Arpitha P Ajay](https://github.com/Arpitha-P-Ajay)

## Link to product walkthrough
https://github.com/user-attachments/assets/ef574fd7-9246-49e2-8462-0ef83556c0ef

## How it Works ?
1. The user visits the homepage (`/`) and selects pizza size and toppings.  
2. On form submission, the data is sent to the FastAPI backend (`/order`).  
3. The backend calculates the **total price** and generates an **order summary**.  
4. The order details (size, toppings, delivery time, status) are displayed back to the user.  

## Libraries used
- **fastapi** – 0.116.1  
- **uvicorn** – 0.35.0  
- **jinja2** – 3.1.6  
- **python-multipart** – 0.0.9  

## How to configure
1. Clone the repository  
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/Mac
   venv\Scripts\activate      # For Windows  
3. Install dependencies:
```bash
   pip install -r requirements.txt
```

 
## How to Run
1. Start the FastAPI server:
 ```bash
   uvicorn main:app --reload
```
2. Open your browser
3. Order your pizza

## Hosted Link
https://pizzaorder-fast-api.onrender.com/

## Screenshots

<img width="959" height="563" alt="image" src="https://github.com/user-attachments/assets/75ab4e21-9b15-46ee-9ab6-ee2d5caa88be" />
<img width="959" height="564" alt="image" src="https://github.com/user-attachments/assets/5c18f8fa-a56f-45a3-a627-6377b934e6c8" />

