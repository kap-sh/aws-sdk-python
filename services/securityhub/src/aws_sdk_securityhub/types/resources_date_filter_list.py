"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesDateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_date_filter

ResourcesDateFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.resources_date_filter.ResourcesDateFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesDateFilterList) -> list:
    import aws_sdk_securityhub.types.resources_date_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.resources_date_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourcesDateFilterList:
    import aws_sdk_securityhub.types.resources_date_filter

    out: ResourcesDateFilterList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.resources_date_filter.deserialize_json(item)
        )
    return out
