"""Generated from Smithy shape ``com.amazonaws.guardduty#CountByResourceType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.long
    import capo_guardduty.types.resource_type

CountByResourceType: TypeAlias = dict[
    "capo_guardduty.types.resource_type.ResourceType", "capo_guardduty.types.long.Long"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CountByResourceType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_guardduty.types.resource_type

        out[capo_guardduty.types.resource_type.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> CountByResourceType:
    out: CountByResourceType = {}
    for key, value in data.items():
        import capo_guardduty.types.resource_type

        out[capo_guardduty.types.resource_type.deserialize_json(key)] = value
    return out
