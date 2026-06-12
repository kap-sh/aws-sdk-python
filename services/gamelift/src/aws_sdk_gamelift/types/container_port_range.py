"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerPortRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.ip_protocol
    import aws_sdk_gamelift.types.port_number


class ContainerPortRange(TypedDict):
    from_port: NotRequired["aws_sdk_gamelift.types.port_number.PortNumber"]
    """<p>A starting value for the range of allowed port numbers.</p>"""
    to_port: NotRequired["aws_sdk_gamelift.types.port_number.PortNumber"]
    """<p>An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than <code>FromPort</code>.</p>"""
    protocol: NotRequired["aws_sdk_gamelift.types.ip_protocol.IpProtocol"]
    """<p>The network protocol that these ports support. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerPortRange) -> dict:
    out: dict = {}
    if "from_port" in value:
        out["FromPort"] = value["from_port"]
    if "to_port" in value:
        out["ToPort"] = value["to_port"]
    if "protocol" in value:
        import aws_sdk_gamelift.types.ip_protocol

        out["Protocol"] = aws_sdk_gamelift.types.ip_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerPortRange:
    out: ContainerPortRange = {}  # type: ignore[typeddict-item]
    if "FromPort" in data:
        out["from_port"] = data["FromPort"]
    if "ToPort" in data:
        out["to_port"] = data["ToPort"]
    if "Protocol" in data:
        import aws_sdk_gamelift.types.ip_protocol

        out["protocol"] = aws_sdk_gamelift.types.ip_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    return out
