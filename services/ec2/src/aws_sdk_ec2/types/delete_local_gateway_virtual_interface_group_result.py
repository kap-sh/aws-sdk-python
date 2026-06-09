"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayVirtualInterfaceGroupResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group


class DeleteLocalGatewayVirtualInterfaceGroupResult(TypedDict):
    local_gateway_virtual_interface_group: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group.LocalGatewayVirtualInterfaceGroup"
    ]
    """<p>Information about the deleted local gateway virtual interface group.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayVirtualInterfaceGroupResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_virtual_interface_group" in value:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_group

        aws_sdk_ec2.types.local_gateway_virtual_interface_group.serialize_ec2_query(
            value["local_gateway_virtual_interface_group"],
            pairs,
            f"{prefix}.LocalGatewayVirtualInterfaceGroup",
        )


def deserialize_ec2_query(el: Element) -> DeleteLocalGatewayVirtualInterfaceGroupResult:
    out: DeleteLocalGatewayVirtualInterfaceGroupResult = {}  # type: ignore[typeddict-item]
    child_local_gateway_virtual_interface_group = el.find(
        "LocalGatewayVirtualInterfaceGroup"
    )
    if child_local_gateway_virtual_interface_group is not None:
        import aws_sdk_ec2.types.local_gateway_virtual_interface_group

        out["local_gateway_virtual_interface_group"] = (
            aws_sdk_ec2.types.local_gateway_virtual_interface_group.deserialize_ec2_query(
                child_local_gateway_virtual_interface_group
            )
        )
    return out
