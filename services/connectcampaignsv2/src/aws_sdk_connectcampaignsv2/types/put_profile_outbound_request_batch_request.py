"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutProfileOutboundRequestBatchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request_list


class PutProfileOutboundRequestBatchRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    profile_outbound_requests: "aws_sdk_connectcampaignsv2.types.profile_outbound_request_list.ProfileOutboundRequestList"


# --- restJson1 ser/de ---
def serialize_json(value: PutProfileOutboundRequestBatchRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request_list

    out["profileOutboundRequests"] = (
        aws_sdk_connectcampaignsv2.types.profile_outbound_request_list.serialize_json(
            value["profile_outbound_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutProfileOutboundRequestBatchRequest:
    out: PutProfileOutboundRequestBatchRequest = {}  # type: ignore[typeddict-item]
    if "profileOutboundRequests" in data:
        import aws_sdk_connectcampaignsv2.types.profile_outbound_request_list

        out["profile_outbound_requests"] = (
            aws_sdk_connectcampaignsv2.types.profile_outbound_request_list.deserialize_json(
                data["profileOutboundRequests"]
            )
        )
    else:
        raise DeserializationError(
            "PutProfileOutboundRequestBatchRequest.profile_outbound_requests required"
        )
    return out
