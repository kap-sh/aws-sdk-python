"""Generated from Smithy shape ``com.amazonaws.devopsagent#EventChannelType``."""

from typing import Literal, TypeAlias, cast

"""<p>Event Channel type</p>"""
EventChannelType: TypeAlias = Literal["webhook",]


# --- restJson1 ser/de ---
def serialize_json(value: EventChannelType) -> str:
    return value


def deserialize_json(data: str) -> EventChannelType:
    return cast(EventChannelType, data)
