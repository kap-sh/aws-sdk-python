"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesTrendsStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_trends_string_filter

ResourcesTrendsStringFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.resources_trends_string_filter.ResourcesTrendsStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesTrendsStringFilterList) -> list:
    import aws_sdk_securityhub.types.resources_trends_string_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.resources_trends_string_filter.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ResourcesTrendsStringFilterList:
    import aws_sdk_securityhub.types.resources_trends_string_filter

    out: ResourcesTrendsStringFilterList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.resources_trends_string_filter.deserialize_json(
                item
            )
        )
    return out
