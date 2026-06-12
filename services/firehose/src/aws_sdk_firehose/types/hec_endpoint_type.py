"""Generated from Smithy shape ``com.amazonaws.firehose#HECEndpointType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

HECEndpointType: TypeAlias = Literal[
    "Raw",
    "Event",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Raw",
        "Event",
    )
)


def serialize_aws_json_1_1(value: HECEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HECEndpointType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HECEndpointType value: {data!r}")
    return cast(HECEndpointType, data)
