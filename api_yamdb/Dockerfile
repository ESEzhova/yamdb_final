
FROM python:3.7-slim

WORKDIR /app/innfra

COPY . .

RUN pip3 install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org --no-cache-dir

CMD ["gunicorn", "api_yamdb.wsgi:application", "--bind", "0:8000" ] 