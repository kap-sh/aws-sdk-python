"""Generated from Smithy shape ``com.amazonaws.mediaconnect#DeregisterGatewayInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.gateway_instance_arn


class DeregisterGatewayInstanceRequest(TypedDict, closed=True):
    force: NotRequired["bool"]
    """<p> Force the deregistration of an instance. Force will deregister an instance, even if there are bridges running on it.</p>"""
    gateway_instance_arn: (
        "aws_sdk_mediaconnect.types.gateway_instance_arn.GatewayInstanceArn"
    )
    """<p> The Amazon Resource Name (ARN) of the gateway that contains the instance that you want to deregister.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterGatewayInstanceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterGatewayInstanceRequest:
    out: DeregisterGatewayInstanceRequest = {}  # type: ignore[typeddict-item]
    return out
