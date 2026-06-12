"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#BinaryFile``."""

import datetime
import decimal
from typing import AsyncIterator, Generic, Iterator, Literal, TypeAlias, TypeVar, cast
from aws_sdk_sagemaker_geospatial.errors import DeserializationError
from aws_sdk_sagemaker_geospatial._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

T = TypeVar("T")
class AnyIterator(AsyncIterator[T], Iterator[T], Generic[T]):
    ...

BinaryFile: TypeAlias = AnyIterator[bytes] | bytes