"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesCompositeFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resources_composite_filter

ResourcesCompositeFilterList: TypeAlias = list[
    "aws_sdk_securityhub.types.resources_composite_filter.ResourcesCompositeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesCompositeFilterList) -> list:
    import aws_sdk_securityhub.types.resources_composite_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.resources_composite_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ResourcesCompositeFilterList:
    import aws_sdk_securityhub.types.resources_composite_filter

    out: ResourcesCompositeFilterList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.resources_composite_filter.deserialize_json(item)
        )
    return out
