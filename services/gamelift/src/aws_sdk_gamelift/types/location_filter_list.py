"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.location_filter

LocationFilterList: TypeAlias = list[
    "aws_sdk_gamelift.types.location_filter.LocationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationFilterList) -> list:
    import aws_sdk_gamelift.types.location_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.location_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationFilterList:
    import aws_sdk_gamelift.types.location_filter

    out: LocationFilterList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.location_filter.deserialize_aws_json_1_1(item)
        )
    return out
