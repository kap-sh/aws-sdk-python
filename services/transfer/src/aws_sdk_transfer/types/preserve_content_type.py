"""Generated from Smithy shape ``com.amazonaws.transfer#PreserveContentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

PreserveContentType: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: PreserveContentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreserveContentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PreserveContentType value: {data!r}")
    return cast(PreserveContentType, data)
