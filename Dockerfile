FROM jupyter/tensorflow-notebook

COPY notebooks /home/$NB_USER/work/notebooks

COPY models /home/$NB_USER/work/models

RUN pip install ipympl

ENTRYPOINT ["jupyter", "lab"]