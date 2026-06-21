"""Generated from Smithy shape ``com.amazonaws.mediaconvert#QueueListBy``."""

from typing import Literal, TypeAlias, cast

"""Optional. When you request a list of queues, you can choose to list them alphabetically by NAME or chronologically by CREATION_DATE. If you don't specify, the service will list them by creation date."""
QueueListBy: TypeAlias = Literal[
    "NAME",
    "CREATION_DATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: QueueListBy) -> str:
    return value


def deserialize_json(data: str) -> QueueListBy:
    return cast(QueueListBy, data)
