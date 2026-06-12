"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.location_model

LocationModelList: TypeAlias = list[
    "aws_sdk_gamelift.types.location_model.LocationModel"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationModelList) -> list:
    import aws_sdk_gamelift.types.location_model

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.location_model.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationModelList:
    import aws_sdk_gamelift.types.location_model

    out: LocationModelList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.location_model.deserialize_aws_json_1_1(item))
    return out
