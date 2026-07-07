"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.max_results
    import aws_sdk_codepipeline.types.next_token
    import aws_sdk_codepipeline.types.resource_arn


class ListTagsForResourceInput(TypedDict, closed=True):
    resource_arn: "aws_sdk_codepipeline.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to get tags for.</p>"""
    next_token: NotRequired["aws_sdk_codepipeline.types.next_token.NextToken"]
    """<p>The token that was returned from the previous API call, which would be used to return the next page of the list. The ListTagsforResource call lists all available tags in one call and does not use pagination.</p>"""
    max_results: NotRequired["aws_sdk_codepipeline.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("ListTagsForResourceInput.resource_arn required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
