"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#EventFilterCondition``."""

from typing import Literal, TypeAlias, cast

"""<p>The condition to use for filtering sessions by events.</p>"""
EventFilterCondition: TypeAlias = Literal["HAS_EVENTS",]


# --- restJson1 ser/de ---
def serialize_json(value: EventFilterCondition) -> str:
    return value


def deserialize_json(data: str) -> EventFilterCondition:
    return cast(EventFilterCondition, data)
