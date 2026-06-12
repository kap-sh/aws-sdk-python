"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationResourceEnum``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

ModificationResourceEnum: TypeAlias = Literal[
    "ROOT_VOLUME",
    "USER_VOLUME",
    "COMPUTE_TYPE",
    "PROTOCOL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROOT_VOLUME",
        "USER_VOLUME",
        "COMPUTE_TYPE",
        "PROTOCOL",
    )
)


def serialize_aws_json_1_1(value: ModificationResourceEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModificationResourceEnum:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModificationResourceEnum value: {data!r}")
    return cast(ModificationResourceEnum, data)
