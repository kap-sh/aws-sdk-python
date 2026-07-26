"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationAttributesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.location_attributes

LocationAttributesList: TypeAlias = list[
    "capo_gamelift.types.location_attributes.LocationAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationAttributesList) -> list:
    import capo_gamelift.types.location_attributes

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.location_attributes.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationAttributesList:
    import capo_gamelift.types.location_attributes

    out: LocationAttributesList = []
    for item in data:
        out.append(
            capo_gamelift.types.location_attributes.deserialize_aws_json_1_1(item)
        )
    return out
