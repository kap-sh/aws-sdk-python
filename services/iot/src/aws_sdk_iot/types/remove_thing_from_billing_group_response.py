"""Generated from Smithy shape ``com.amazonaws.iot#RemoveThingFromBillingGroupResponse``."""

from typing_extensions import TypedDict


class RemoveThingFromBillingGroupResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemoveThingFromBillingGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemoveThingFromBillingGroupResponse:
    out: RemoveThingFromBillingGroupResponse = {}  # type: ignore[typeddict-item]
    return out
