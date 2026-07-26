"""Generated from Smithy shape ``com.amazonaws.devopsagent#EventChannelConfiguration``."""

from typing_extensions import TypedDict


class EventChannelConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: EventChannelConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> EventChannelConfiguration:
    out: EventChannelConfiguration = {}  # type: ignore[typeddict-item]
    return out
