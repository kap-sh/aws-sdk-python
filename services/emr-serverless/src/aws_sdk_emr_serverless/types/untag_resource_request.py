"""Generated from Smithy shape ``com.amazonaws.emrserverless#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.resource_arn
    import aws_sdk_emr_serverless.types.tag_key_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_emr_serverless.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) that identifies the resource to list the tags for. Currently, the supported resources are Amazon EMR Serverless applications and job runs.</p>"""
    tag_keys: "aws_sdk_emr_serverless.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
