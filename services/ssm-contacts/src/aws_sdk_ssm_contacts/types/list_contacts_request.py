"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListContactsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.contact_alias
    import aws_sdk_ssm_contacts.types.contact_type
    import aws_sdk_ssm_contacts.types.max_results
    import aws_sdk_ssm_contacts.types.pagination_token


class ListContactsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "aws_sdk_ssm_contacts.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token to continue to the next page of results.</p>"""
    max_results: NotRequired["aws_sdk_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of contacts and escalation plans per page of results.</p>"""
    alias_prefix: NotRequired["aws_sdk_ssm_contacts.types.contact_alias.ContactAlias"]
    """<p>Used to list only contacts who's aliases start with the specified prefix.</p>"""
    type: NotRequired["aws_sdk_ssm_contacts.types.contact_type.ContactType"]
    """<p>The type of contact.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContactsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "alias_prefix" in value:
        out["AliasPrefix"] = value["alias_prefix"]
    if "type" in value:
        import aws_sdk_ssm_contacts.types.contact_type

        out["Type"] = aws_sdk_ssm_contacts.types.contact_type.serialize_aws_json_1_1(
            value["type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContactsRequest:
    out: ListContactsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "AliasPrefix" in data:
        out["alias_prefix"] = data["AliasPrefix"]
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.contact_type

        out["type"] = aws_sdk_ssm_contacts.types.contact_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    return out
