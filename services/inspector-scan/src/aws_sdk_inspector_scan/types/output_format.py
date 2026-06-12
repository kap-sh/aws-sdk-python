"""Generated from Smithy shape ``com.amazonaws.inspectorscan#OutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector_scan.errors import DeserializationError

OutputFormat: TypeAlias = Literal[
    "CYCLONE_DX_1_5",
    "INSPECTOR",
    "INSPECTOR_ALT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CYCLONE_DX_1_5",
        "INSPECTOR",
        "INSPECTOR_ALT",
    )
)


def serialize_json(value: OutputFormat) -> str:
    return value


def deserialize_json(data: str) -> OutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputFormat value: {data!r}")
    return cast(OutputFormat, data)
