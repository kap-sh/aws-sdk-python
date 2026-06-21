"""Generated from Smithy shape ``com.amazonaws.workdocs#SubscriptionType``."""

from typing import Literal, TypeAlias, cast

SubscriptionType: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: SubscriptionType) -> str:
    return value


def deserialize_json(data: str) -> SubscriptionType:
    return cast(SubscriptionType, data)
