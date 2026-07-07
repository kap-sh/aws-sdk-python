"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mwaa_serverless.types.taggable_resource_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "aws_sdk_mwaa_serverless.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
