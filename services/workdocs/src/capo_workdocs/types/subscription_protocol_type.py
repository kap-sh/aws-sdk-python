"""Generated from Smithy shape ``com.amazonaws.workdocs#SubscriptionProtocolType``."""

from typing import Literal, TypeAlias, cast

SubscriptionProtocolType: TypeAlias = Literal[
    "HTTPS",
    "SQS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionProtocolType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionProtocolType:
    return cast(SubscriptionProtocolType, data)
