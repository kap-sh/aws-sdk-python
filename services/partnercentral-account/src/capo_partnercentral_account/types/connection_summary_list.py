"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.connection_summary

ConnectionSummaryList: TypeAlias = list[
    "capo_partnercentral_account.types.connection_summary.ConnectionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionSummaryList) -> list:
    import capo_partnercentral_account.types.connection_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_account.types.connection_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectionSummaryList:
    import capo_partnercentral_account.types.connection_summary

    out: ConnectionSummaryList = []
    for item in data:
        out.append(
            capo_partnercentral_account.types.connection_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
