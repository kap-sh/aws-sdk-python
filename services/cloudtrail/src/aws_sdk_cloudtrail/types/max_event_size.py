"""Generated from Smithy shape ``com.amazonaws.cloudtrail#MaxEventSize``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

MaxEventSize: TypeAlias = Literal[
    "Standard",
    "Large",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "Large",
    )
)


def serialize_aws_json_1_1(value: MaxEventSize) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaxEventSize:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaxEventSize value: {data!r}")
    return cast(MaxEventSize, data)
