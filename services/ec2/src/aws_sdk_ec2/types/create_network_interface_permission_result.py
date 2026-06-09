"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfacePermissionResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_permission


class CreateNetworkInterfacePermissionResult(TypedDict):
    interface_permission: NotRequired[
        "aws_sdk_ec2.types.network_interface_permission.NetworkInterfacePermission"
    ]
    """<p>Information about the permission for the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInterfacePermissionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "interface_permission" in value:
        import aws_sdk_ec2.types.network_interface_permission

        aws_sdk_ec2.types.network_interface_permission.serialize_ec2_query(
            value["interface_permission"], pairs, f"{prefix}.InterfacePermission"
        )


def deserialize_ec2_query(el: Element) -> CreateNetworkInterfacePermissionResult:
    out: CreateNetworkInterfacePermissionResult = {}  # type: ignore[typeddict-item]
    child_interface_permission = el.find("InterfacePermission")
    if child_interface_permission is not None:
        import aws_sdk_ec2.types.network_interface_permission

        out["interface_permission"] = (
            aws_sdk_ec2.types.network_interface_permission.deserialize_ec2_query(
                child_interface_permission
            )
        )
    return out
