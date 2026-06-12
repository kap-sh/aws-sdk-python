"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DiagnosticsMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

DiagnosticsMode: TypeAlias = Literal[
    "OFF",
    "SEND_ACTIVE_DTCS",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "SEND_ACTIVE_DTCS",
    )
)


def serialize_aws_json_1_0(value: DiagnosticsMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DiagnosticsMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiagnosticsMode value: {data!r}")
    return cast(DiagnosticsMode, data)
