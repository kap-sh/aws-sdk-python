"""Generated from Smithy shape ``com.amazonaws.datazone#RuleAction``."""

from typing import Literal, TypeAlias, cast

RuleAction: TypeAlias = Literal[
    "CREATE_LISTING_CHANGE_SET",
    "CREATE_SUBSCRIPTION_REQUEST",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleAction) -> str:
    return value


def deserialize_json(data: str) -> RuleAction:
    return cast(RuleAction, data)
