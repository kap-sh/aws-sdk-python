"""Generated from Smithy shape ``com.amazonaws.mediaconnect#BatchGetRouterNetworkInterfaceError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.router_network_interface_arn


class BatchGetRouterNetworkInterfaceError(TypedDict):
    arn: "aws_sdk_mediaconnect.types.router_network_interface_arn.RouterNetworkInterfaceArn"
    """<p>The Amazon Resource Name (ARN) of the router network interface for which the error occurred.</p>"""
    code: "str"
    """<p>The error code associated with the error.</p>"""
    message: "str"
    """<p>A message describing the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRouterNetworkInterfaceError) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchGetRouterNetworkInterfaceError:
    out: BatchGetRouterNetworkInterfaceError = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("BatchGetRouterNetworkInterfaceError.arn required")
    if "code" in data:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BatchGetRouterNetworkInterfaceError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError(
            "BatchGetRouterNetworkInterfaceError.message required"
        )
    return out
