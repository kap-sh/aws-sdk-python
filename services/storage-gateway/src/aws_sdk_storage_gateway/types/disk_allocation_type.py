"""Generated from Smithy shape ``com.amazonaws.storagegateway#DiskAllocationType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_storage_gateway.errors import DeserializationError
from aws_sdk_storage_gateway._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

"""<p>One of the <code>DiskAllocationType</code> enumeration values that identifies how a local disk is used.</p> <p>Valid Values: <code>UPLOAD_BUFFER</code> | <code>CACHE_STORAGE</code> </p>"""
DiskAllocationType: TypeAlias = str
