"""Generated from Smithy shape ``com.amazonaws.supplychain#ClientToken``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_supplychain.errors import DeserializationError
from aws_sdk_supplychain._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
ClientToken: TypeAlias = str