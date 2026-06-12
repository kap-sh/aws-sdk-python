"""Generated from Smithy shape ``com.amazonaws.gamelift#ConnectionPortRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.port_number


class ConnectionPortRange(TypedDict):
    from_port: NotRequired["aws_sdk_gamelift.types.port_number.PortNumber"]
    """<p>Starting value for the port range.</p>"""
    to_port: NotRequired["aws_sdk_gamelift.types.port_number.PortNumber"]
    """<p>Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than <code>FromPort</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionPortRange) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionPortRange:
    out: ConnectionPortRange = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    return out
