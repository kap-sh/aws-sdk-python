"""Generated from Smithy shape ``com.amazonaws.cloud9#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloud9.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloud9.types.environment_arn
    import aws_sdk_cloud9.types.tag_list


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_cloud9.types.environment_arn.EnvironmentArn"
    """<p>The Amazon Resource Name (ARN) of the Cloud9 development environment to add tags to.</p>"""
    tags: "aws_sdk_cloud9.types.tag_list.TagList"
    """<p>The list of tags to add to the given Cloud9 development environment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import aws_sdk_cloud9.types.tag_list

    out["Tags"] = aws_sdk_cloud9.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("TagResourceRequest.resource_arn required")
    if "Tags" in data:
        import aws_sdk_cloud9.types.tag_list

        out["tags"] = aws_sdk_cloud9.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
