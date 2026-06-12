"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesNumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_number_filter

ResourcesNumberFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.resources_number_filter.ResourcesNumberFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesNumberFilterList) -> list:
    import aws_sdk_securityhub.types.resources_number_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.resources_number_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourcesNumberFilterList:
    import aws_sdk_securityhub.types.resources_number_filter

    out: ResourcesNumberFilterList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.resources_number_filter.deserialize_json(item)
        )
    return out
