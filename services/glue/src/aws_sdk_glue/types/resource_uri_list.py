"""Generated from Smithy shape ``com.amazonaws.glue#ResourceUriList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.resource_uri

ResourceUriList: TypeAlias = list["aws_sdk_glue.types.resource_uri.ResourceUri"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUriList) -> list:
    import aws_sdk_glue.types.resource_uri

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.resource_uri.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ResourceUriList:
    import aws_sdk_glue.types.resource_uri

    out: ResourceUriList = []
    for item in data:
        out.append(aws_sdk_glue.types.resource_uri.deserialize_aws_json_1_1(item))
    return out
