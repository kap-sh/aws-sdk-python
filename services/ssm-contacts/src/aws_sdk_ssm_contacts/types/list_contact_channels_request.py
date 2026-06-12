"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListContactChannelsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.max_results
    import aws_sdk_ssm_contacts.types.pagination_token
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class ListContactChannelsRequest(TypedDict):
    contact_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact.</p>"""
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token to continue to the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of contact channels per page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContactChannelsRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContactChannelsRequest:
    out: ListContactChannelsRequest = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("ListContactChannelsRequest.contact_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
