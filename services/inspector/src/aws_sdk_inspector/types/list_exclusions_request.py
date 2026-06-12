"""Generated from Smithy shape ``com.amazonaws.inspector#ListExclusionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.arn
    import aws_sdk_inspector.types.list_max_results
    import aws_sdk_inspector.types.pagination_token


class ListExclusionsRequest(TypedDict):
    assessment_run_arn: "aws_sdk_inspector.types.arn.Arn"
    """<p>The ARN of the assessment run that generated the exclusions that you want to list.</p>"""
    next_token: NotRequired["aws_sdk_inspector.types.pagination_token.PaginationToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the ListExclusionsRequest action. Subsequent calls to the action fill nextToken in the request with the value of nextToken from the previous response to continue listing data.</p>"""
    max_results: NotRequired["aws_sdk_inspector.types.list_max_results.ListMaxResults"]
    """<p>You can use this parameter to indicate the maximum number of items you want in the response. The default value is 100. The maximum value is 500.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListExclusionsRequest) -> dict:
    out: dict = {}
    out["assessmentRunArn"] = value["assessment_run_arn"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListExclusionsRequest:
    out: ListExclusionsRequest = {}  # type: ignore[typeddict-item]
    if "assessmentRunArn" in data:
        out["assessment_run_arn"] = data["assessmentRunArn"]
    else:
        raise DeserializationError("ListExclusionsRequest.assessment_run_arn required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
