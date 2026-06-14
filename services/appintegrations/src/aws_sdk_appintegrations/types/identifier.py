"""Generated from Smithy shape ``com.amazonaws.appintegrations#Identifier``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_appintegrations.errors import DeserializationError
from aws_sdk_appintegrations._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

Identifier: TypeAlias = str