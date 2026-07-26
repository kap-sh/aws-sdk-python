"""Generated from Smithy shape ``com.amazonaws.support#DescribeCommunicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_support.errors import DeserializationError

if TYPE_CHECKING:
    import capo_support.types.after_time
    import capo_support.types.before_time
    import capo_support.types.case_id
    import capo_support.types.max_results
    import capo_support.types.next_token


class DescribeCommunicationsRequest(TypedDict, closed=True):
    case_id: "capo_support.types.case_id.CaseId"
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-2013-c4c1d2bf33c5cf47</i> </p>"""
    before_time: NotRequired["capo_support.types.before_time.BeforeTime"]
    """<p>The end date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>"""
    after_time: NotRequired["capo_support.types.after_time.AfterTime"]
    """<p>The start date for a filtered date search on support case communications. Case communications are available for 12 months after creation.</p>"""
    next_token: NotRequired["capo_support.types.next_token.NextToken"]
    """<p>A resumption point for pagination.</p>"""
    max_results: NotRequired["capo_support.types.max_results.MaxResults"]
    """<p>The maximum number of results to return before paginating.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCommunicationsRequest) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    if "before_time" in value:
        out["beforeTime"] = value["before_time"]
    if "after_time" in value:
        out["afterTime"] = value["after_time"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCommunicationsRequest:
    out: DescribeCommunicationsRequest = {}  # type: ignore[typeddict-item]
    if "caseId" in data:
        out["case_id"] = data["caseId"]
    else:
        raise DeserializationError("DescribeCommunicationsRequest.case_id required")
    if "beforeTime" in data:
        out["before_time"] = data["beforeTime"]
    if "afterTime" in data:
        out["after_time"] = data["afterTime"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
