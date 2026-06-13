"""Generated from Smithy shape ``com.amazonaws.securityir#ListCommentsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_security_ir.types.case_id


class ListCommentsRequest(TypedDict):
    next_token: NotRequired["str"]
    """<p>An optional string that, if supplied, must be copied from the output of a previous call to ListComments. When provided in this manner, the API fetches the next page of results. </p>"""
    max_results: NotRequired["int"]
    """<p>Optional element for ListComments to limit the number of responses.</p>"""
    case_id: "aws_sdk_security_ir.types.case_id.CaseId"
    """<p>Required element for ListComments to designate the case to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommentsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 25)
    return out


def deserialize_json(data: dict) -> ListCommentsRequest:
    out: ListCommentsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 25
    return out
