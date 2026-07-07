"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ListPartnerEventSourceAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.next_token
    import aws_sdk_cloudwatch_events.types.partner_event_source_account_list


class ListPartnerEventSourceAccountsResponse(TypedDict, closed=True):
    partner_event_source_accounts: NotRequired[
        "aws_sdk_cloudwatch_events.types.partner_event_source_account_list.PartnerEventSourceAccountList"
    ]
    """<p>The list of partner event sources returned by the operation.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_events.types.next_token.NextToken"]
    """<p>A token you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPartnerEventSourceAccountsResponse) -> dict:
    out: dict = {}
    if "partner_event_source_accounts" in value:
        import aws_sdk_cloudwatch_events.types.partner_event_source_account_list

        out["PartnerEventSourceAccounts"] = (
            aws_sdk_cloudwatch_events.types.partner_event_source_account_list.serialize_aws_json_1_1(
                value["partner_event_source_accounts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPartnerEventSourceAccountsResponse:
    out: ListPartnerEventSourceAccountsResponse = {}  # type: ignore[typeddict-item]
    if "PartnerEventSourceAccounts" in data:
        import aws_sdk_cloudwatch_events.types.partner_event_source_account_list

        out["partner_event_source_accounts"] = (
            aws_sdk_cloudwatch_events.types.partner_event_source_account_list.deserialize_aws_json_1_1(
                data["PartnerEventSourceAccounts"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
