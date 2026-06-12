"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#TagFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.tag_filter

TagFilters: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.tag_filter.TagFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagFilters) -> list:
    import aws_sdk_application_discovery_service.types.tag_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.tag_filter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TagFilters:
    import aws_sdk_application_discovery_service.types.tag_filter

    out: TagFilters = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.tag_filter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
