import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb
from apikey import API_KEY

movie = Movie()
tmdb = TMDb()
tmdb.api_key = API_KEY

