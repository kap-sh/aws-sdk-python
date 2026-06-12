"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListLinkedWhatsAppBusinessAccountsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary_list
    import aws_sdk_socialmessaging.types.next_token


class ListLinkedWhatsAppBusinessAccountsOutput(TypedDict):
    linked_accounts: NotRequired[
        "aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary_list.LinkedWhatsAppBusinessAccountSummaryList"
    ]
    """<p>A list of WhatsApp Business Accounts linked to your Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_socialmessaging.types.next_token.NextToken"]
    """<p>The next token for pagination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinkedWhatsAppBusinessAccountsOutput) -> dict:
    out: dict = {}
    if "linked_accounts" in value:
        import aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary_list

        out["linkedAccounts"] = (
            aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary_list.serialize_json(
                value["linked_accounts"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLinkedWhatsAppBusinessAccountsOutput:
    out: ListLinkedWhatsAppBusinessAccountsOutput = {}  # type: ignore[typeddict-item]
    if "linkedAccounts" in data:
        import aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary_list

        out["linked_accounts"] = (
            aws_sdk_socialmessaging.types.linked_whats_app_business_account_summary_list.deserialize_json(
                data["linkedAccounts"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
