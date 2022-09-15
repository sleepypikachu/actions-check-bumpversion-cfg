FROM python:3.8

COPY src/* /

ENTRYPOINT ["/usr/local/bin/python", "/check_bumpversion_cfg.py"]
