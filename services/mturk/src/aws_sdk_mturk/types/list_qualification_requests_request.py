"""Generated from Smithy shape ``com.amazonaws.mturk#ListQualificationRequestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.entity_id
    import aws_sdk_mturk.types.pagination_token
    import aws_sdk_mturk.types.result_size


class ListQualificationRequestsRequest(TypedDict, closed=True):
    qualification_type_id: NotRequired["aws_sdk_mturk.types.entity_id.EntityId"]
    """<p>The ID of the QualificationType.</p>"""
    next_token: NotRequired["aws_sdk_mturk.types.pagination_token.PaginationToken"]
    max_results: NotRequired["aws_sdk_mturk.types.result_size.ResultSize"]
    """<p> The maximum number of results to return in a single call. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListQualificationRequestsRequest) -> dict:
    out: dict = {}
    if "qualification_type_id" in value:
        out["QualificationTypeId"] = value["qualification_type_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListQualificationRequestsRequest:
    out: ListQualificationRequestsRequest = {}  # type: ignore[typeddict-item]
    if "QualificationTypeId" in data:
        out["qualification_type_id"] = data["QualificationTypeId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
