#!/usr/bin/python3
from models.base import BaseData, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

class Order(BaseData, Base):
    """Order Data Model"""
    __tablename__ = 'orders'
    user_id = Column(String(60), ForeignKey('users.id'), primary_key=True)
    plan_id = Column(String(60), ForeignKey('plans.id'), primary_key=True)

    # Define many-to-many relationship with Meals
    meals = relationship("Meal", secondary="order_meals",  overlaps="orders")
    preferences = relationship("Preference", secondary="order_preferences", overlaps="orders")
    order_meals = relationship("OrderMeal", overlaps="meals")
