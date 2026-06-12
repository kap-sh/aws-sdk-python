"""Generated from Smithy shape ``com.amazonaws.datasync#LocationFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datasync.types.location_filter

LocationFilters: TypeAlias = list[
    "aws_sdk_datasync.types.location_filter.LocationFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationFilters) -> list:
    import aws_sdk_datasync.types.location_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_datasync.types.location_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LocationFilters:
    import aws_sdk_datasync.types.location_filter

    out: LocationFilters = []
    for item in data:
        out.append(
            aws_sdk_datasync.types.location_filter.deserialize_aws_json_1_1(item)
        )
    return out
