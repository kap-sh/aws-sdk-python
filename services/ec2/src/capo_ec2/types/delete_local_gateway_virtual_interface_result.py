"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayVirtualInterfaceResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_virtual_interface


class DeleteLocalGatewayVirtualInterfaceResult(TypedDict, closed=True):
    local_gateway_virtual_interface: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface.LocalGatewayVirtualInterface"
    ]
    """<p>Information about the deleted local gateway virtual interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayVirtualInterfaceResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_virtual_interface" in value:
        import capo_ec2.types.local_gateway_virtual_interface

        capo_ec2.types.local_gateway_virtual_interface.serialize_ec2_query(
            value["local_gateway_virtual_interface"],
            pairs,
            f"{key_prefix}LocalGatewayVirtualInterface",
        )


def deserialize_ec2_query(el: Element) -> DeleteLocalGatewayVirtualInterfaceResult:
    out: DeleteLocalGatewayVirtualInterfaceResult = {}  # type: ignore[typeddict-item]
    child_local_gateway_virtual_interface = el.find("localGatewayVirtualInterface")
    if child_local_gateway_virtual_interface is not None:
        import capo_ec2.types.local_gateway_virtual_interface

        out["local_gateway_virtual_interface"] = (
            capo_ec2.types.local_gateway_virtual_interface.deserialize_ec2_query(
                child_local_gateway_virtual_interface
            )
        )
    return out
