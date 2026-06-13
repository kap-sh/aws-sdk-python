"""Generated from Smithy shape ``com.amazonaws.ssmsap#OperationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

OperationMode: TypeAlias = Literal[
    "PRIMARY",
    "LOGREPLAY",
    "DELTA_DATASHIPPING",
    "LOGREPLAY_READACCESS",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "LOGREPLAY",
        "DELTA_DATASHIPPING",
        "LOGREPLAY_READACCESS",
        "NONE",
    )
)


def serialize_json(value: OperationMode) -> str:
    return value


def deserialize_json(data: str) -> OperationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationMode value: {data!r}")
    return cast(OperationMode, data)
