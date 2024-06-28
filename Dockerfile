FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
RUN echo "Now starting the app. It may take a few seconds ..."
CMD ["tradingview-new.py"]
