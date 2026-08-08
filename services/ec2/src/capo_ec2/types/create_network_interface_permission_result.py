"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfacePermissionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_interface_permission


class CreateNetworkInterfacePermissionResult(TypedDict, closed=True):
    interface_permission: NotRequired[
        "capo_ec2.types.network_interface_permission.NetworkInterfacePermission"
    ]
    """<p>Information about the permission for the network interface.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInterfacePermissionResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "interface_permission" in value:
        import capo_ec2.types.network_interface_permission

        capo_ec2.types.network_interface_permission.serialize_ec2_query(
            value["interface_permission"], pairs, f"{key_prefix}InterfacePermission"
        )


def deserialize_ec2_query(el: Element) -> CreateNetworkInterfacePermissionResult:
    out: CreateNetworkInterfacePermissionResult = {}  # type: ignore[typeddict-item]
    child_interface_permission = el.find("interfacePermission")
    if child_interface_permission is not None:
        import capo_ec2.types.network_interface_permission

        out["interface_permission"] = (
            capo_ec2.types.network_interface_permission.deserialize_ec2_query(
                child_interface_permission
            )
        )
    return out
