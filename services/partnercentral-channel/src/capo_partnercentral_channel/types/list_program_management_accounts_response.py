"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListProgramManagementAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.next_token
    import capo_partnercentral_channel.types.program_management_account_summaries


class ListProgramManagementAccountsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_partnercentral_channel.types.program_management_account_summaries.ProgramManagementAccountSummaries"
    ]
    """<p>List of program management accounts matching the criteria.</p>"""
    next_token: NotRequired["capo_partnercentral_channel.types.next_token.NextToken"]
    """<p>Token for retrieving the next page of results, if available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProgramManagementAccountsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_partnercentral_channel.types.program_management_account_summaries

        out["items"] = (
            capo_partnercentral_channel.types.program_management_account_summaries.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListProgramManagementAccountsResponse:
    out: ListProgramManagementAccountsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_partnercentral_channel.types.program_management_account_summaries

        out["items"] = (
            capo_partnercentral_channel.types.program_management_account_summaries.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
