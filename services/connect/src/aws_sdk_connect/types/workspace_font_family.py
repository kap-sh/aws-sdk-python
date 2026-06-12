"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceFontFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

WorkspaceFontFamily: TypeAlias = Literal[
    "Arial",
    "Courier New",
    "Georgia",
    "Times New Roman",
    "Trebuchet",
    "Verdana",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Arial",
        "Courier New",
        "Georgia",
        "Times New Roman",
        "Trebuchet",
        "Verdana",
    )
)


def serialize_json(value: WorkspaceFontFamily) -> str:
    return value


def deserialize_json(data: str) -> WorkspaceFontFamily:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspaceFontFamily value: {data!r}")
    return cast(WorkspaceFontFamily, data)
