"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListContactsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.contacts_list
    import capo_ssm_contacts.types.pagination_token


class ListContactsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The pagination token to continue to the next page of results.</p>"""
    contacts: NotRequired["capo_ssm_contacts.types.contacts_list.ContactsList"]
    """<p>A list of the contacts and escalation plans in your Incident Manager account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContactsResult) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "contacts" in value:
        import capo_ssm_contacts.types.contacts_list

        out["Contacts"] = capo_ssm_contacts.types.contacts_list.serialize_aws_json_1_1(
            value["contacts"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContactsResult:
    out: ListContactsResult = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Contacts" in data:
        import capo_ssm_contacts.types.contacts_list

        out["contacts"] = (
            capo_ssm_contacts.types.contacts_list.deserialize_aws_json_1_1(
                data["Contacts"]
            )
        )
    return out
