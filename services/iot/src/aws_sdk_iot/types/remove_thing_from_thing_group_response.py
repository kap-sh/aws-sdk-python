"""Generated from Smithy shape ``com.amazonaws.iot#RemoveThingFromThingGroupResponse``."""

from typing_extensions import TypedDict


class RemoveThingFromThingGroupResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemoveThingFromThingGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveThingFromThingGroupResponse:
    out: RemoveThingFromThingGroupResponse = {}  # type: ignore[typeddict-item]
    return out
