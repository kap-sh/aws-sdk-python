"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.location_string_model

LocationList: TypeAlias = list[
    "aws_sdk_gamelift.types.location_string_model.LocationStringModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LocationList:
    return list(data)
