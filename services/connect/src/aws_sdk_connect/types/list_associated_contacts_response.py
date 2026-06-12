"""Generated from Smithy shape ``com.amazonaws.connect#ListAssociatedContactsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.associated_contact_summary_list
    import aws_sdk_connect.types.next_token


class ListAssociatedContactsResponse(TypedDict):
    contact_summary_list: NotRequired[
        "aws_sdk_connect.types.associated_contact_summary_list.AssociatedContactSummaryList"
    ]
    """<p>List of the contact summary for all the contacts in contact tree associated with unique identifier.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssociatedContactsResponse) -> dict:
    out: dict = {}
    if "contact_summary_list" in value:
        import aws_sdk_connect.types.associated_contact_summary_list

        out["ContactSummaryList"] = (
            aws_sdk_connect.types.associated_contact_summary_list.serialize_json(
                value["contact_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssociatedContactsResponse:
    out: ListAssociatedContactsResponse = {}  # type: ignore[typeddict-item]
    if "ContactSummaryList" in data:
        import aws_sdk_connect.types.associated_contact_summary_list

        out["contact_summary_list"] = (
            aws_sdk_connect.types.associated_contact_summary_list.deserialize_json(
                data["ContactSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
