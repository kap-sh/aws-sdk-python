"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#PortOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.port_number


class PortOverride(TypedDict, closed=True):
    listener_port: NotRequired[
        "aws_sdk_global_accelerator.types.port_number.PortNumber"
    ]
    """<p>The listener port that you want to map to a specific endpoint port. This is the port that user traffic arrives to the Global Accelerator on.</p>"""
    endpoint_port: NotRequired[
        "aws_sdk_global_accelerator.types.port_number.PortNumber"
    ]
    """<p>The endpoint port that you want a listener port to be mapped to. This is the port on the endpoint, such as the Application Load Balancer or Amazon EC2 instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortOverride) -> dict:
    out: dict = {}
    if "listener_port" in value:
        out["ListenerPort"] = value["listener_port"]
    if "endpoint_port" in value:
        out["EndpointPort"] = value["endpoint_port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PortOverride:
    out: PortOverride = {}  # type: ignore[typeddict-item]
    if "ListenerPort" in data:
        out["listener_port"] = data["ListenerPort"]
    if "EndpointPort" in data:
        out["endpoint_port"] = data["EndpointPort"]
    return out
