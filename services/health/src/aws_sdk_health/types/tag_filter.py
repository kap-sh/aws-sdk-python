"""Generated from Smithy shape ``com.amazonaws.health#tagFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_health.types.tag_set

tagFilter: TypeAlias = list["aws_sdk_health.types.tag_set.tagSet"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: tagFilter) -> list:
    import aws_sdk_health.types.tag_set

    out: list = []
    for item in value:
        out.append(aws_sdk_health.types.tag_set.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> tagFilter:
    import aws_sdk_health.types.tag_set

    out: tagFilter = []
    for item in data:
        out.append(aws_sdk_health.types.tag_set.deserialize_aws_json_1_1(item))
    return out
