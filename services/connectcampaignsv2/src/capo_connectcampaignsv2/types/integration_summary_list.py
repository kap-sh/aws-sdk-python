"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#IntegrationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.integration_summary

IntegrationSummaryList: TypeAlias = list[
    "capo_connectcampaignsv2.types.integration_summary.IntegrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummaryList) -> list:
    import capo_connectcampaignsv2.types.integration_summary

    out: list = []
    for item in value:
        out.append(
            capo_connectcampaignsv2.types.integration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IntegrationSummaryList:
    import capo_connectcampaignsv2.types.integration_summary

    out: IntegrationSummaryList = []
    for item in data:
        out.append(
            capo_connectcampaignsv2.types.integration_summary.deserialize_json(item)
        )
    return out
