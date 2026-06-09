"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.protocol_value


class TransitGatewayConnectOptions(TypedDict):
    protocol: NotRequired["aws_sdk_ec2.types.protocol_value.ProtocolValue"]
    """<p>The tunnel protocol.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayConnectOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "protocol" in value:
        import aws_sdk_ec2.types.protocol_value

        aws_sdk_ec2.types.protocol_value.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayConnectOptions:
    out: TransitGatewayConnectOptions = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import aws_sdk_ec2.types.protocol_value

        out["protocol"] = aws_sdk_ec2.types.protocol_value.deserialize_ec2_query(
            child_protocol
        )
    return out
