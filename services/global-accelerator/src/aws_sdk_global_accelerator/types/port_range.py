"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#PortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.port_number


class PortRange(TypedDict, closed=True):
    from_port: NotRequired["aws_sdk_global_accelerator.types.port_number.PortNumber"]
    """<p>The first port in the range of ports, inclusive.</p>"""
    to_port: NotRequired["aws_sdk_global_accelerator.types.port_number.PortNumber"]
    """<p>The last port in the range of ports, inclusive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortRange) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PortRange:
    out: PortRange = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    return out
