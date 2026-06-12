"""Generated from Smithy shape ``com.amazonaws.connectcases#ListCasesForContactRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.contact_arn
    import aws_sdk_connectcases.types.domain_id
    import aws_sdk_connectcases.types.next_token


class ListCasesForContactRequest(TypedDict):
    domain_id: "aws_sdk_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    contact_arn: "aws_sdk_connectcases.types.contact_arn.ContactArn"
    """<p>A unique identifier of a contact in Amazon Connect.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesForContactRequest) -> dict:
    out: dict = {}
    out["contactArn"] = value["contact_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCasesForContactRequest:
    out: ListCasesForContactRequest = {}  # type: ignore[typeddict-item]
    if "contactArn" in data:
        out["contact_arn"] = data["contactArn"]
    else:
        raise DeserializationError("ListCasesForContactRequest.contact_arn required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
