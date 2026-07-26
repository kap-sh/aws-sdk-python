"""Generated from Smithy shape ``com.amazonaws.iot#DeprecateThingTypeResponse``."""

from typing_extensions import TypedDict


class DeprecateThingTypeResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeprecateThingTypeResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeprecateThingTypeResponse:
    out: DeprecateThingTypeResponse = {}  # type: ignore[typeddict-item]
    return out
