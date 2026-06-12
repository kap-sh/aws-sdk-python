"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListConnectionInvitationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.connection_invitation_summary_list
    import aws_sdk_partnercentral_account.types.next_token


class ListConnectionInvitationsResponse(TypedDict):
    connection_invitation_summaries: "aws_sdk_partnercentral_account.types.connection_invitation_summary_list.ConnectionInvitationSummaryList"
    """<p>A list of connection invitation summaries matching the specified criteria.</p>"""
    next_token: NotRequired["aws_sdk_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results if more results are available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionInvitationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_account.types.connection_invitation_summary_list

    out["ConnectionInvitationSummaries"] = (
        aws_sdk_partnercentral_account.types.connection_invitation_summary_list.serialize_aws_json_1_0(
            value["connection_invitation_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionInvitationsResponse:
    out: ListConnectionInvitationsResponse = {}  # type: ignore[typeddict-item]
    if "ConnectionInvitationSummaries" in data:
        import aws_sdk_partnercentral_account.types.connection_invitation_summary_list

        out["connection_invitation_summaries"] = (
            aws_sdk_partnercentral_account.types.connection_invitation_summary_list.deserialize_aws_json_1_0(
                data["ConnectionInvitationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListConnectionInvitationsResponse.connection_invitation_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
