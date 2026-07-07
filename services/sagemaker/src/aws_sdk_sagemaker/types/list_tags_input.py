"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTagsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.list_tags_max_results
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.resource_arn


class ListTagsInput(TypedDict, closed=True):
    resource_arn: NotRequired["aws_sdk_sagemaker.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the resource whose tags you want to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p> If the response to the previous <code>ListTags</code> request is truncated, SageMaker returns this token. To retrieve the next set of tags, use it in the subsequent request. </p>"""
    max_results: NotRequired[
        "aws_sdk_sagemaker.types.list_tags_max_results.ListTagsMaxResults"
    ]
    """<p>Maximum number of tags to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsInput) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsInput:
    out: ListTagsInput = {}  # type: ignore[typeddict-item]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
