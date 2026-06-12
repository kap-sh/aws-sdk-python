"""Generated from Smithy shape ``com.amazonaws.storagegateway#Role``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage.</p>"""
Role: TypeAlias = str
