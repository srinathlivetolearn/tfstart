FROM jupyter/tensorflow-notebook

COPY notebooks /home/$NB_USER/work/notebooks

COPY models /home/$NB_USER/work/models

RUN pip install ipympl

RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager

RUN jupyter labextension install  jupyter-matplotlib

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab"]