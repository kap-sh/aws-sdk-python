"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#PutDialRequestBatchResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.failed_request_list
    import aws_sdk_connectcampaigns.types.successful_request_list


class PutDialRequestBatchResponse(TypedDict):
    successful_requests: NotRequired[
        "aws_sdk_connectcampaigns.types.successful_request_list.SuccessfulRequestList"
    ]
    failed_requests: NotRequired[
        "aws_sdk_connectcampaigns.types.failed_request_list.FailedRequestList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PutDialRequestBatchResponse) -> dict:
    out: dict = {}
    if "successful_requests" in value:
        import aws_sdk_connectcampaigns.types.successful_request_list

        out["successfulRequests"] = (
            aws_sdk_connectcampaigns.types.successful_request_list.serialize_json(
                value["successful_requests"]
            )
        )
    if "failed_requests" in value:
        import aws_sdk_connectcampaigns.types.failed_request_list

        out["failedRequests"] = (
            aws_sdk_connectcampaigns.types.failed_request_list.serialize_json(
                value["failed_requests"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutDialRequestBatchResponse:
    out: PutDialRequestBatchResponse = {}  # type: ignore[typeddict-item]
    if "successfulRequests" in data:
        import aws_sdk_connectcampaigns.types.successful_request_list

        out["successful_requests"] = (
            aws_sdk_connectcampaigns.types.successful_request_list.deserialize_json(
                data["successfulRequests"]
            )
        )
    if "failedRequests" in data:
        import aws_sdk_connectcampaigns.types.failed_request_list

        out["failed_requests"] = (
            aws_sdk_connectcampaigns.types.failed_request_list.deserialize_json(
                data["failedRequests"]
            )
        )
    return out
