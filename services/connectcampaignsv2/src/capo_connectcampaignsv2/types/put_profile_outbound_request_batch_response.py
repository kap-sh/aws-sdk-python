"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutProfileOutboundRequestBatchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.failed_profile_outbound_request_list
    import capo_connectcampaignsv2.types.successful_profile_outbound_request_list


class PutProfileOutboundRequestBatchResponse(TypedDict, closed=True):
    successful_requests: NotRequired[
        "capo_connectcampaignsv2.types.successful_profile_outbound_request_list.SuccessfulProfileOutboundRequestList"
    ]
    failed_requests: NotRequired[
        "capo_connectcampaignsv2.types.failed_profile_outbound_request_list.FailedProfileOutboundRequestList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutProfileOutboundRequestBatchResponse) -> dict:
    out: dict = {}
    if "successful_requests" in value:
        import capo_connectcampaignsv2.types.successful_profile_outbound_request_list

        out["successfulRequests"] = (
            capo_connectcampaignsv2.types.successful_profile_outbound_request_list.serialize_json(
                value["successful_requests"]
            )
        )
    if "failed_requests" in value:
        import capo_connectcampaignsv2.types.failed_profile_outbound_request_list

        out["failedRequests"] = (
            capo_connectcampaignsv2.types.failed_profile_outbound_request_list.serialize_json(
                value["failed_requests"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutProfileOutboundRequestBatchResponse:
    out: PutProfileOutboundRequestBatchResponse = {}  # type: ignore[typeddict-item]
    if "successfulRequests" in data:
        import capo_connectcampaignsv2.types.successful_profile_outbound_request_list

        out["successful_requests"] = (
            capo_connectcampaignsv2.types.successful_profile_outbound_request_list.deserialize_json(
                data["successfulRequests"]
            )
        )
    if "failedRequests" in data:
        import capo_connectcampaignsv2.types.failed_profile_outbound_request_list

        out["failed_requests"] = (
            capo_connectcampaignsv2.types.failed_profile_outbound_request_list.deserialize_json(
                data["failedRequests"]
            )
        )
    return out
