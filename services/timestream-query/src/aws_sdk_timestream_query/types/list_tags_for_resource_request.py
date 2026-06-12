"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_timestream_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_query.types.amazon_resource_name
    import aws_sdk_timestream_query.types.max_tags_for_resource_result
    import aws_sdk_timestream_query.types.next_tags_for_resource_results_token


class ListTagsForResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The Timestream resource with tags to be listed. This value is an Amazon Resource Name (ARN).</p>"""
    max_results: NotRequired[
        "aws_sdk_timestream_query.types.max_tags_for_resource_result.MaxTagsForResourceResult"
    ]
    """<p>The maximum number of tags to return.</p>"""
    next_token: NotRequired[
        "aws_sdk_timestream_query.types.next_tags_for_resource_results_token.NextTagsForResourceResultsToken"
    ]
    """<p>A pagination token to resume pagination.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    else:
        raise DeserializationError("ListTagsForResourceRequest.resource_arn required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
