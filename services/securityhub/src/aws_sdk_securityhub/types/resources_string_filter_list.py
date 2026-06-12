"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_string_filter

ResourcesStringFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.resources_string_filter.ResourcesStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesStringFilterList) -> list:
    import aws_sdk_securityhub.types.resources_string_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.resources_string_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourcesStringFilterList:
    import aws_sdk_securityhub.types.resources_string_filter

    out: ResourcesStringFilterList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.resources_string_filter.deserialize_json(item)
        )
    return out
