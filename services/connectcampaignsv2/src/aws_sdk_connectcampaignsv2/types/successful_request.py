"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SuccessfulRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.client_token
    import aws_sdk_connectcampaignsv2.types.dial_request_id


class SuccessfulRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "aws_sdk_connectcampaignsv2.types.client_token.ClientToken"
    ]
    id: NotRequired["aws_sdk_connectcampaignsv2.types.dial_request_id.DialRequestId"]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> SuccessfulRequest:
    out: SuccessfulRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "id" in data:
        out["id"] = data["id"]
    return out
