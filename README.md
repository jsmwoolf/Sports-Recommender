# Sports-Recommender
Python program that determines the ideal sport based off of certain attributes.

## Installation

To install the required libraries, do the following:

### With pip
```
pip install pandas
```

__Note__: You might need to add `sudo` if you don't have elevated privileges.  You might also need to specify `pip3` instead of `pip` if you're running Python 3.

### With conda

pandas is already installed with Anaconda.  There is no additional steps needed.

## Running the script

The following commands can be used to run the Python script:

```
cd ./Sports-Recommender
python recommender.py
```

# Extra
Below are a few notes about the dataset.

## Attributes
The attributes that are used to recommend a sport is as defined from ESPN:

* __Endurance__: The ability to continue to perform a skill or action for long periods of time. Example: Lance Armstrong
* __Strength__: The ability to produce force. Example: NFL linebackers.
* __Power__: The ability to produce strength in the shortest possible time. Example: Barry Bonds.
* __Speed__: The ability to move quickly. Example: Marion Jones, Maurice Green.
* __Agility__: The ability to change direction quickly. Example: Derek Jeter, Mia Hamm.
* __Flexibility__: The ability to stretch the joints across a large range of motion. Example: Gymnasts, divers.
* __Nerve__: The ability to overcome fear. Example: High-board divers, race-car drivers, ski jumpers.
* __Durability__: The ability to withstand physical punishment over a long period of time. Example: NBA/NHL players.
* __Hand-Eye Coordination__: The ability to react quickly to sensory perception. Example: A hitter reacting to a breaking pitch; a drag racer timing acceleration to the green light.
* __Analytic Aptitude__: The ability to evaluate and react appropriately to strategic situations. Example: Joe Montana reading a defense; basketball point guard on a fast break.

## Dataset Source
The original dataset is from a page from [ESPN](http://www.espn.com/espn/page2/sportSkills).

The dataset file was retrieved from [data.word](https://data.world/coreyhermanson/toughest-sport-by-skill).
