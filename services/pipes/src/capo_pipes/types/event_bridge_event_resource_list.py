"""Generated from Smithy shape ``com.amazonaws.pipes#EventBridgeEventResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pipes.types.arn_or_json_path

EventBridgeEventResourceList: TypeAlias = list[
    "capo_pipes.types.arn_or_json_path.ArnOrJsonPath"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeEventResourceList) -> list:
    return list(value)


def deserialize_json(data: list) -> EventBridgeEventResourceList:
    return list(data)
