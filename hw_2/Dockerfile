FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends texlive-latex-base texlive-fonts-recommended texlive-plain-generic texlive-latex-extra latexmk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY . /app
WORKDIR /app

CMD python generate_tex_file.py 4 7 artifacts/example_image.png > artifacts/task_2_2_docker.tex && \
    pdflatex -output-directory artifacts artifacts/task_2_2_docker.tex

