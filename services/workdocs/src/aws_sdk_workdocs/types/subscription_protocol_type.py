"""Generated from Smithy shape ``com.amazonaws.workdocs#SubscriptionProtocolType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

SubscriptionProtocolType: TypeAlias = Literal[
    "HTTPS",
    "SQS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTPS",
        "SQS",
    )
)


def serialize_json(value: SubscriptionProtocolType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionProtocolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SubscriptionProtocolType value: {data!r}")
    return cast(SubscriptionProtocolType, data)
