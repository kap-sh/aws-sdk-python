"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionInvitationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.connection_invitation_summary

ConnectionInvitationSummaryList: TypeAlias = list[
    "capo_partnercentral_account.types.connection_invitation_summary.ConnectionInvitationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionInvitationSummaryList) -> list:
    import capo_partnercentral_account.types.connection_invitation_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_account.types.connection_invitation_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectionInvitationSummaryList:
    import capo_partnercentral_account.types.connection_invitation_summary

    out: ConnectionInvitationSummaryList = []
    for item in data:
        out.append(
            capo_partnercentral_account.types.connection_invitation_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
