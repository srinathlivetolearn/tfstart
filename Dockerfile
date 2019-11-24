FROM jupyter/tensorflow-notebook

COPY notebooks /home/$NB_USER/work

COPY models /home/$NB_USER/work

ENTRYPOINT ["jupyter", "lab"]