# McPlayHD API Wrapper For Python
### Functions
#### Get FastBuilder Leaderboards
- Any Position (1-50)
- Any Mode
#### Get FastBuilder Stats For A Certain Player And Game Mode
- Best Time
- Average Time
- Total Attempts
- Total Successful Attempts
- Verified Status
- [Speedrun.com](https://speedrun.com/McPlayHD) Verified Status
#### Get Player Info
- Rank
#### Debug Info
- Response Time
- Rate Limits
- Token Auth Check
### Soon To Come (McPlayHD Needs to Update API First.)
#### Get MineSweeper Stats For A Certain Player
- Rank
- Points In Season
- Best Time
- Average Time
- Total Attempts
- Total Successful Attempts
- Total Mines Defused
### Installation

This library is hosted on [PyPI](https://pypi.org).
You can use the following commands to install it.
```sh
pip install mcplaystats
```

To Use it In a Python Project

```python
from mcplaystats import statistics,player,debug
```
### Use Of Functions
Example of Getting FastBuilder PB & Average Time for Notch in Game Mode Short

```python
from mcplaystats import statistics,player,debug
notchsBestTime = statistics.fb_stats_pb("SHORT","Notch",<your api token>)
notchsAvgTime = statistics.fb_stats_avg("SHORT","Notch",<your api token>)
```

Example of Getting Minesweeper PB & Average Time for Notch in Current Season

```python
from mcplaystats import statistics,player,debug
notchsBestTime = statistics.ms_stats_pb("Notch",<your api token>,"current")
notchsAvgTime = statistics.ms_stats_avg("Notch",<your api token>,"current")
```
### License

MIT
