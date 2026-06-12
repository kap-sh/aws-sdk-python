"""Generated from Smithy shape ``com.amazonaws.fms#ResourceTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.resource_tag

ResourceTags: TypeAlias = list["aws_sdk_fms.types.resource_tag.ResourceTag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceTags) -> list:
    import aws_sdk_fms.types.resource_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.resource_tag.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceTags:
    import aws_sdk_fms.types.resource_tag

    out: ResourceTags = []
    for item in data:
        out.append(aws_sdk_fms.types.resource_tag.deserialize_aws_json_1_1(item))
    return out
