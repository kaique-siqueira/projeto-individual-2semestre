import speedtest
import time


st = speedtest.Speedtest()

st.get_best_server()

#print(f"Your ping is: {round(st.results.ping, 0)} ms")
#print(f"Your ping is: {round(st.results.ping *2, 0)} ms * 2")
print(f"Your download speed: {round(st.download() / 1000 / 1000, 1)} Mbit/s")
print(f"Your download speed: {round(st.download() / 1000 / 1000 * 0.5, 1)} Mbit/s *2")
#print(f"Your upload speed: {round(st.upload() / 1000 / 1000, 1)} Mbit/s")
