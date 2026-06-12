"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#FailedProfileOutboundRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.client_token
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request_failure_code
    import aws_sdk_connectcampaignsv2.types.profile_outbound_request_id


class FailedProfileOutboundRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_connectcampaignsv2.types.client_token.ClientToken"
    ]
    id: NotRequired[
        "aws_sdk_connectcampaignsv2.types.profile_outbound_request_id.ProfileOutboundRequestId"
    ]
    failure_code: NotRequired[
        "aws_sdk_connectcampaignsv2.types.profile_outbound_request_failure_code.ProfileOutboundRequestFailureCode"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FailedProfileOutboundRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "id" in value:
        out["id"] = value["id"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> FailedProfileOutboundRequest:
    out: FailedProfileOutboundRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "id" in data:
        out["id"] = data["id"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    return out
