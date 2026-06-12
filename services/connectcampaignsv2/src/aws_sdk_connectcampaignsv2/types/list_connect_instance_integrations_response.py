"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ListConnectInstanceIntegrationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.integration_summary_list
    import aws_sdk_connectcampaignsv2.types.next_token


class ListConnectInstanceIntegrationsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_connectcampaignsv2.types.next_token.NextToken"]
    integration_summary_list: NotRequired[
        "aws_sdk_connectcampaignsv2.types.integration_summary_list.IntegrationSummaryList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListConnectInstanceIntegrationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "integration_summary_list" in value:
        import aws_sdk_connectcampaignsv2.types.integration_summary_list

        out["integrationSummaryList"] = (
            aws_sdk_connectcampaignsv2.types.integration_summary_list.serialize_json(
                value["integration_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListConnectInstanceIntegrationsResponse:
    out: ListConnectInstanceIntegrationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "integrationSummaryList" in data:
        import aws_sdk_connectcampaignsv2.types.integration_summary_list

        out["integration_summary_list"] = (
            aws_sdk_connectcampaignsv2.types.integration_summary_list.deserialize_json(
                data["integrationSummaryList"]
            )
        )
    return out
