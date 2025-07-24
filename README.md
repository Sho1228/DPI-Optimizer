# Mouse Sensitivity Tester

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)<br>
A Python application created to help users find their optimal mouse sensitivity by testing reaction time and accuracy with delayed mouse cursor movement.

## Features

- **Fullscreen Testing Environment**: Black background with randomly appearing white circles
- **Customizable Mouse Delay**: Adjustable cursor delay (default: 0.5 seconds, range: 0.0-2.0s)
- **Variable Circle Size**: Customizable target size for different difficulty levels
- **Performance Tracking**: Real-time accuracy statistics and hit rate
- **Visual Feedback**: Green dot shows delayed mouse position
- **Random Spawn Pattern**: Circles appear at random intervals and locations

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

The program will launch in fullscreen mode. Click on the white circles as they appear to test your accuracy with the delayed mouse cursor.

## Controls

| Key | Action |
|-----|--------|
| `S` | Toggle settings panel |
| `Q` | Increase circle size |
| `A` | Decrease circle size |
| `W` | Increase mouse delay |
| `Z` | Decrease mouse delay |
| `E` | Increase circle timeout |
| `D` | Decrease circle timeout |
| `R` | Reset statistics |
| `ESC` | Exit application |

## Customizable Settings

### Mouse Delay
- **Range**: 0.0 - 2.0 seconds
- **Default**: 0.5 seconds
- **Purpose**: Simulates the delay between mouse movement and cursor response

### Circle Size
- **Range**: 5 - 100 pixels radius
- **Default**: 25 pixels
- **Purpose**: Adjusts target difficulty

### Circle Timeout
- **Range**: 0.5 - 5.0 seconds
- **Default**: 2.0 seconds
- **Purpose**: How long circles stay visible before disappearing


## How It Works

1. White circles spawn randomly across the screen at intervals between 0.5-2.5 seconds
2. Your mouse cursor appears as a green dot with the configured delay
3. Click on circles before they disappear (configurable timeout)
4. Track your accuracy to find optimal sensitivity settings

## Finding Your Optimal Sensitivity

1. Start with default settings (0.5s delay, 25px circles)
2. Adjust your mouse DPI/sensitivity in your system settings
3. Test different combinations and note your accuracy
4. Experiment with different delays to simulate various gaming scenarios
5. Use smaller circles for precision training, larger for reaction time

## Requirements

- Python 3.6+
- Pygame library
- Display capable of 1920x1080 resolution (adjustable in code)
