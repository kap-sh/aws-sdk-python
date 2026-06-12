"""Generated from Smithy shape ``com.amazonaws.glue#ListUsageProfilesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.orchestration_page_size200
    import aws_sdk_glue.types.orchestration_token


class ListUsageProfilesRequest(TypedDict):
    next_token: NotRequired["aws_sdk_glue.types.orchestration_token.OrchestrationToken"]
    """<p>A continuation token, included if this is a continuation call.</p>"""
    max_results: NotRequired[
        "aws_sdk_glue.types.orchestration_page_size200.OrchestrationPageSize200"
    ]
    """<p>The maximum number of usage profiles to return in a single response.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListUsageProfilesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListUsageProfilesRequest:
    out: ListUsageProfilesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
