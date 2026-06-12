"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#AzureApplicationId``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_pca_connector_scep.errors import DeserializationError
from aws_sdk_pca_connector_scep._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

AzureApplicationId: TypeAlias = str