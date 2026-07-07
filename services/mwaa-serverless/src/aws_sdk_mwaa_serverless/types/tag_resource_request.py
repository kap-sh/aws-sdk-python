"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_mwaa_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.taggable_resource_arn
    import aws_sdk_mwaa_serverless.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to which to add tags.</p>"""
    tags: "aws_sdk_mwaa_serverless.types.tags.Tags"
    """<p>A map of tags to add to the resource. Each tag consists of a key-value pair.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_mwaa_serverless.types.tags

    out["Tags"] = aws_sdk_mwaa_serverless.types.tags.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_mwaa_serverless.types.tags

        out["tags"] = aws_sdk_mwaa_serverless.types.tags.deserialize_aws_json_1_0(
            data["Tags"]
        )
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
