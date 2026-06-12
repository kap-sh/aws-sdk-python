"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#Tags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.tag

Tags: TypeAlias = list["aws_sdk_opensearchserverless.types.tag.Tag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tags) -> list:
    import aws_sdk_opensearchserverless.types.tag

    out: list = []
    for item in value:
        out.append(aws_sdk_opensearchserverless.types.tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Tags:
    import aws_sdk_opensearchserverless.types.tag

    out: Tags = []
    for item in data:
        out.append(
            aws_sdk_opensearchserverless.types.tag.deserialize_aws_json_1_0(item)
        )
    return out
