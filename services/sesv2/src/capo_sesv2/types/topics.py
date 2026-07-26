"""Generated from Smithy shape ``com.amazonaws.sesv2#Topics``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.topic

Topics: TypeAlias = list["capo_sesv2.types.topic.Topic"]


# --- restJson1 ser/de ---
def serialize_json(value: Topics) -> list:
    import capo_sesv2.types.topic

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.topic.serialize_json(item))
    return out


def deserialize_json(data: list) -> Topics:
    import capo_sesv2.types.topic

    out: Topics = []
    for item in data:
        out.append(capo_sesv2.types.topic.deserialize_json(item))
    return out
