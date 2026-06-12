"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#PutDialRequestBatchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id
    import aws_sdk_connectcampaigns.types.dial_request_list


class PutDialRequestBatchRequest(TypedDict):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"
    dial_requests: "aws_sdk_connectcampaigns.types.dial_request_list.DialRequestList"


# --- restJson1 ser/de ---
def serialize_json(value: PutDialRequestBatchRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectcampaigns.types.dial_request_list

    out["dialRequests"] = (
        aws_sdk_connectcampaigns.types.dial_request_list.serialize_json(
            value["dial_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutDialRequestBatchRequest:
    out: PutDialRequestBatchRequest = {}  # type: ignore[typeddict-item]
    if "dialRequests" in data:
        import aws_sdk_connectcampaigns.types.dial_request_list

        out["dial_requests"] = (
            aws_sdk_connectcampaigns.types.dial_request_list.deserialize_json(
                data["dialRequests"]
            )
        )
    else:
        raise DeserializationError("PutDialRequestBatchRequest.dial_requests required")
    return out
