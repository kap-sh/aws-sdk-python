"""Generated from Smithy shape ``com.amazonaws.mq#ChangeType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of change pending for the ActiveMQ user.</p>"""
ChangeType: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    return cast(ChangeType, data)
