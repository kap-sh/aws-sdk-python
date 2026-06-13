"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeleteGatewayResponse``."""

from typing import TypedDict

from typing_extensions import NotRequired


class DeleteGatewayResponse(TypedDict):
    gateway_arn: NotRequired["str"]
    """<p> The ARN of the gateway that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayResponse) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    return out


def deserialize_json(data: dict) -> DeleteGatewayResponse:
    out: DeleteGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gatewayArn" in data:
        out["gateway_arn"] = data["gatewayArn"]
    return out
