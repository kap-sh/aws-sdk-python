"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfacePermissionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_interface_permission_list
    import capo_ec2.types.string


class DescribeNetworkInterfacePermissionsResult(TypedDict, closed=True):
    network_interface_permissions: NotRequired[
        "capo_ec2.types.network_interface_permission_list.NetworkInterfacePermissionList"
    ]
    """<p>The network interface permissions.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInterfacePermissionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_permissions" in value:
        import capo_ec2.types.network_interface_permission_list

        capo_ec2.types.network_interface_permission_list.serialize_ec2_query(
            value["network_interface_permissions"],
            pairs,
            f"{key_prefix}NetworkInterfacePermissions",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInterfacePermissionsResult:
    out: DescribeNetworkInterfacePermissionsResult = {}  # type: ignore[typeddict-item]
    if el.find("networkInterfacePermissions") is not None:
        import capo_ec2.types.network_interface_permission_list

        out["network_interface_permissions"] = (
            capo_ec2.types.network_interface_permission_list.deserialize_ec2_query(
                el, "networkInterfacePermissions"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
