"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeregisterGatewayInstanceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.instance_state


class DeregisterGatewayInstanceResponse(TypedDict):
    gateway_instance_arn: NotRequired["str"]
    """<p> The ARN of the instance.</p>"""
    instance_state: NotRequired[
        "aws_sdk_mediaconnect.types.instance_state.InstanceState"
    ]
    """<p> The status of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterGatewayInstanceResponse) -> dict:
    out: dict = {}
    if "gateway_instance_arn" in value:
        out["gatewayInstanceArn"] = value["gateway_instance_arn"]
    if "instance_state" in value:
        import aws_sdk_mediaconnect.types.instance_state

        out["instanceState"] = aws_sdk_mediaconnect.types.instance_state.serialize_json(
            value["instance_state"]
        )
    return out


def deserialize_json(data: dict) -> DeregisterGatewayInstanceResponse:
    out: DeregisterGatewayInstanceResponse = {}  # type: ignore[typeddict-item]
    if "gatewayInstanceArn" in data:
        out["gateway_instance_arn"] = data["gatewayInstanceArn"]
    if "instanceState" in data:
        import aws_sdk_mediaconnect.types.instance_state

        out["instance_state"] = (
            aws_sdk_mediaconnect.types.instance_state.deserialize_json(
                data["instanceState"]
            )
        )
    return out
