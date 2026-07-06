"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutOutboundRequestBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.outbound_request_list


class PutOutboundRequestBatchRequest(TypedDict, closed=True):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    outbound_requests: (
        "aws_sdk_connectcampaignsv2.types.outbound_request_list.OutboundRequestList"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PutOutboundRequestBatchRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaignsv2.types.outbound_request_list

    out["outboundRequests"] = (
        aws_sdk_connectcampaignsv2.types.outbound_request_list.serialize_json(
            value["outbound_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutOutboundRequestBatchRequest:
    out: PutOutboundRequestBatchRequest = {}  # type: ignore[typeddict-item]
    if "outboundRequests" in data:
        import aws_sdk_connectcampaignsv2.types.outbound_request_list

        out["outbound_requests"] = (
            aws_sdk_connectcampaignsv2.types.outbound_request_list.deserialize_json(
                data["outboundRequests"]
            )
        )
    else:
        raise DeserializationError(
            "PutOutboundRequestBatchRequest.outbound_requests required"
        )
    return out
