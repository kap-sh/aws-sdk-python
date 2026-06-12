"""Generated from Smithy shape ``com.amazonaws.dsql#ClientToken``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_dsql.errors import DeserializationError
from aws_sdk_dsql._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>Idempotency token so a request is only processed once.</p>"""
ClientToken: TypeAlias = str