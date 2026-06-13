"""Generated from Smithy shape ``com.amazonaws.rtbfabric#UpdateRequesterGatewayResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_rtbfabric.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.gateway_id
    import aws_sdk_rtbfabric.types.requester_gateway_status


class UpdateRequesterGatewayResponse(TypedDict):
    gateway_id: "aws_sdk_rtbfabric.types.gateway_id.GatewayId"
    """<p>The unique identifier of the gateway.</p>"""
    status: "aws_sdk_rtbfabric.types.requester_gateway_status.RequesterGatewayStatus"
    """<p>The status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRequesterGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    import aws_sdk_rtbfabric.types.requester_gateway_status

    out["status"] = aws_sdk_rtbfabric.types.requester_gateway_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRequesterGatewayResponse:
    out: UpdateRequesterGatewayResponse = {}  # type: ignore[typeddict-item]
    if "gatewayId" in data:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError("UpdateRequesterGatewayResponse.gateway_id required")
    if "status" in data:
        import aws_sdk_rtbfabric.types.requester_gateway_status

        out["status"] = (
            aws_sdk_rtbfabric.types.requester_gateway_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateRequesterGatewayResponse.status required")
    return out
