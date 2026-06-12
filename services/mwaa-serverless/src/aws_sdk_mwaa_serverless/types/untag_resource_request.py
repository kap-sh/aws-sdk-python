"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.tag_keys
    import aws_sdk_mwaa_serverless.types.taggable_resource_arn


class UntagResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>"""
    tag_keys: "aws_sdk_mwaa_serverless.types.tag_keys.TagKeys"
    """<p>A list of tag keys to remove from the resource. Only the keys are required; the values are ignored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
