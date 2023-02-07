import pytube, sys

def banner():
	print("""
 \033[1;31m___ ___ __    __       \033[1;32m___ ___
\033[1;31m|   Y   |__.--|  |\033[1;0m_____\033[1;32m(   Y   )
\033[1;31m|.  |   |  |  _  |\033[1;0m______\033[1;32m\  1  /
\033[1;31m|.  |   |__|_____|      \033[1;32m/  _  \ 
\033[1;31m|:  1   |              \033[1;32m/:  |   \ 
 \033[1;31m\:.. ./              \033[1;32m(::. |:.  )
  \033[1;31m`---'                \033[1;32m`--- ---'
\033[0m+----------------------+
\033[0m| \033[1;32m>>> \033[1;36mCoded by BEC \033[1;32m<<< \033[0m|
\033[0m+----------------------+""")
banner()

try:
	url = input("\033[1;32mMasukkan URL video : \033[0m")

	if url == "":
		print("\033[1;31mInvalid URL")
		sys.exit()

	y = pytube.YouTube(url)

	print(y.streams.get_highest_resolution().download("/sdcard"))
	print("\033[1;33m>>> \033[1;32mDownload was successful!\n\033[1;33m>>> \033[1;32mTersimpan di internal storage.")
	print("\033[0m+--------------+")
	print("\033[0m| \033[1;33m>>> \033[1;32mData \033[1;33m<<< \033[0m|")
	print("\033[0m+--------------+")
	print("\033[1;32mJudul : \033[0m",y.title)
	print("\033[1;32mDeskripsi video : \033[0m",y.description)
	print("\033[1;32mPenayangan : \033[0m",y.views)
	print("\033[1;32mDurasi video : \033[0m",y.length)
	print("\033[1;32mTanggal publikasi : \033[0m",y.publish_date)
	print("\033[1;32mDibatasi usia : \033[0m",y.age_restricted)
	print("\033[1;32mRating : \033[0m",y.rating)
	print("\033[1;32mTag yg digunakan : \033[0m",y.keywords)
	print("\033[1;32mURL thumbnail : \033[0m",y.thumbnail_url)
	print("\033[1;32mNama channel : \033[0m",y.author)
	print("\033[1;32mID channel : \033[0m",y.channel_id)
	print("\033[1;32mURL channel : \033[0m",y.channel_url)

except KeyboardInterrupt:
	print("\033[1;33mOk I understand")
