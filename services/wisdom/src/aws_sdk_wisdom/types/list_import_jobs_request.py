"""Generated from Smithy shape ``com.amazonaws.wisdom#ListImportJobsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.max_results
    import aws_sdk_wisdom.types.non_empty_string
    import aws_sdk_wisdom.types.uuid_or_arn


class ListImportJobsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_wisdom.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    knowledge_base_id: "aws_sdk_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if you're storing Wisdom Content resource to it. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListImportJobsRequest:
    out: ListImportJobsRequest = {}  # type: ignore[typeddict-item]
    return out
