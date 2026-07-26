"""Generated from Smithy shape ``com.amazonaws.kafka#TopicState``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of a topic request.</p>"""
TopicState: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TopicState) -> str:
    return value


def deserialize_json(data: str) -> TopicState:
    return cast(TopicState, data)
