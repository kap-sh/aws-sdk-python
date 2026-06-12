"""Generated from Smithy shape ``com.amazonaws.costexplorer#SubscriberStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

SubscriberStatus: TypeAlias = Literal[
    "CONFIRMED",
    "DECLINED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFIRMED",
        "DECLINED",
    )
)


def serialize_aws_json_1_1(value: SubscriberStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SubscriberStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriberStatus value: {data!r}")
    return cast(SubscriberStatus, data)
