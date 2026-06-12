"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListPageResolutionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.pagination_token
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class ListPageResolutionsRequest(TypedDict):
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""
    page_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact engaged for the incident.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPageResolutionsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["PageId"] = value["page_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPageResolutionsRequest:
    out: ListPageResolutionsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PageId" in data:
        out["page_id"] = data["PageId"]
    else:
        raise DeserializationError("ListPageResolutionsRequest.page_id required")
    return out
