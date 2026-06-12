"""Generated from Smithy shape ``com.amazonaws.location#EutranCellId``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_location.errors import DeserializationError
from aws_sdk_location._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

EutranCellId: TypeAlias = int

DEFAULT_EUTRAN_CELL_ID: EutranCellId = 0