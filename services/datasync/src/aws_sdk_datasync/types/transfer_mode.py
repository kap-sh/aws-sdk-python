"""Generated from Smithy shape ``com.amazonaws.datasync#TransferMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

TransferMode: TypeAlias = Literal[
    "CHANGED",
    "ALL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHANGED",
        "ALL",
    )
)


def serialize_aws_json_1_1(value: TransferMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransferMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransferMode value: {data!r}")
    return cast(TransferMode, data)
