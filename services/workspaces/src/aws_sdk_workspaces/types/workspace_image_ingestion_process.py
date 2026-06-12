"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageIngestionProcess``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_workspaces.errors import DeserializationError
from aws_sdk_workspaces._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

WorkspaceImageIngestionProcess: TypeAlias = Literal[
    "BYOL_REGULAR",
    "BYOL_GRAPHICS",
    "BYOL_GRAPHICSPRO",
    "BYOL_GRAPHICS_G4DN",
    "BYOL_REGULAR_WSP",
    "BYOL_GRAPHICS_G4DN_WSP",
    "BYOL_REGULAR_BYOP",
    "BYOL_GRAPHICS_G4DN_BYOP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BYOL_REGULAR",
        "BYOL_GRAPHICS",
        "BYOL_GRAPHICSPRO",
        "BYOL_GRAPHICS_G4DN",
        "BYOL_REGULAR_WSP",
        "BYOL_GRAPHICS_G4DN_WSP",
        "BYOL_REGULAR_BYOP",
        "BYOL_GRAPHICS_G4DN_BYOP",
    )
)


def serialize_aws_json_1_1(value: WorkspaceImageIngestionProcess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceImageIngestionProcess:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WorkspaceImageIngestionProcess value: {data!r}"
        )
    return cast(WorkspaceImageIngestionProcess, data)
