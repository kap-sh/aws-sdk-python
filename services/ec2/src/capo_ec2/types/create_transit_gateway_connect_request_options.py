"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectRequestOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.protocol_value


class CreateTransitGatewayConnectRequestOptions(TypedDict, closed=True):
    protocol: NotRequired["capo_ec2.types.protocol_value.ProtocolValue"]
    """<p>The tunnel protocol.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayConnectRequestOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "protocol" in value:
        import capo_ec2.types.protocol_value

        capo_ec2.types.protocol_value.serialize_ec2_query(
            value["protocol"], pairs, f"{prefix}.Protocol"
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayConnectRequestOptions:
    out: CreateTransitGatewayConnectRequestOptions = {}  # type: ignore[typeddict-item]
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_ec2.types.protocol_value

        out["protocol"] = capo_ec2.types.protocol_value.deserialize_ec2_query(
            child_protocol
        )
    return out
