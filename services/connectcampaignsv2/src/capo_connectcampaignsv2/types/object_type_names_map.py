"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ObjectTypeNamesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.event_type
    import capo_connectcampaignsv2.types.object_type_name

ObjectTypeNamesMap: TypeAlias = dict[
    "capo_connectcampaignsv2.types.event_type.EventType",
    "capo_connectcampaignsv2.types.object_type_name.ObjectTypeName",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ObjectTypeNamesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ObjectTypeNamesMap:
    out: ObjectTypeNamesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
