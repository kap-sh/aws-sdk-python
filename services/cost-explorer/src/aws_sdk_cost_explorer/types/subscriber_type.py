"""Generated from Smithy shape ``com.amazonaws.costexplorer#SubscriberType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

SubscriberType: TypeAlias = Literal[
    "EMAIL",
    "SNS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL",
        "SNS",
    )
)


def serialize_aws_json_1_1(value: SubscriberType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriberType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriberType value: {data!r}")
    return cast(SubscriberType, data)
