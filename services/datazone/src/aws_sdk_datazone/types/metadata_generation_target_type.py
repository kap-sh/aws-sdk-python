"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationTargetType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_datazone.errors import DeserializationError
from aws_sdk_datazone._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

MetadataGenerationTargetType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ASSET",))


def serialize_json(value: MetadataGenerationTargetType) -> str:
    return value


def deserialize_json(data: str) -> MetadataGenerationTargetType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MetadataGenerationTargetType value: {data!r}"
        )
    return cast(MetadataGenerationTargetType, data)
