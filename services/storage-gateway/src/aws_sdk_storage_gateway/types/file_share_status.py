"""Generated from Smithy shape ``com.amazonaws.storagegateway#FileShareStatus``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The status of the file share.</p> <p>Valid Values: <code>CREATING</code> | <code>UPDATING</code> | <code>AVAILABLE</code> | <code>DELETING</code> </p>"""
FileShareStatus: TypeAlias = str
