#!/usr/bin/env python3
from game_engine import GameEngine
from config import Config
import asyncio
def main():
      cfg=Config()
      game=GameEngine(cfg)
      asyncio.run(game.start())
  if __name__=="__main__":
        main()
