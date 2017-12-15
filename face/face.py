# -*- coding: utf-8 -*-
from FACe_signer import FACe_signer
import zeep

# FACe environments
FACE_ENVS = {
    'prod': "https://webservice.face.gob.es/facturasspp2?wsdl",
    'staging': "https://se-face-webservice.redsara.es/facturasspp2?wsdl",
}

class FACe(object):
    def __init__(self, **kwargs):
        assert "certificate" in kwargs and type(kwargs['certificate']) == str, "The certificate filename for requests signing must be defined"
        self.certificate = kwargs['certificate']

        self.debug = True
        # Handle optional kwarg
        if 'debug' in kwargs:
            assert type(kwargs['debug']) == bool, "debug argument must be a boolean"
            self.debug = kwargs['debug']

        # initialize a ZEEP client with the desired FACe envs
        self.client = zeep.Client(
            FACE_ENVS['staging'],
            plugins=[FACe_signer(self.certificate, debug=self.debug)]
        )

    def list_nifs(self):
        self.client.service.consultarNIFs()
