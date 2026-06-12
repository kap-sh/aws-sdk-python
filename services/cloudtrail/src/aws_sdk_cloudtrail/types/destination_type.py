"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

DestinationType: TypeAlias = Literal[
    "EVENT_DATA_STORE",
    "AWS_SERVICE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVENT_DATA_STORE",
        "AWS_SERVICE",
    )
)


def serialize_aws_json_1_1(value: DestinationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DestinationType value: {data!r}")
    return cast(DestinationType, data)
