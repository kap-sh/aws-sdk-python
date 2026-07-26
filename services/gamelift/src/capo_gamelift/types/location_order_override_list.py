"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationOrderOverrideList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.location_string_model

LocationOrderOverrideList: TypeAlias = list[
    "capo_gamelift.types.location_string_model.LocationStringModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationOrderOverrideList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LocationOrderOverrideList:
    return list(data)
