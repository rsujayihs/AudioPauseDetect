from pydub import AudioSegment
from pydub.silence import detect_silence
from pydub.silence import detect_nonsilent

sound = AudioSegment.from_file("C:/Users/sujay/Downloads/Chapter-1.wav", format="wav")

silent_ranges = detect_silence(sound, min_silence_len=100, silence_thresh=-30)
print(len(silent_ranges))
for start, end in silent_ranges:
    print(start/1000.0, end/1000.0)

non_silent_ranges = detect_nonsilent(sound, min_silence_len=500, silence_thresh=-30)
print(len(nonsilent_ranges))
for start, end in nonsilent_ranges:
    print(start/1000.0, end/1000.0)
