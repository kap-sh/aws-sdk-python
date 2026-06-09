"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfacePermissionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_permission_list
    import aws_sdk_ec2.types.string


class DescribeNetworkInterfacePermissionsResult(TypedDict):
    network_interface_permissions: NotRequired[
        "aws_sdk_ec2.types.network_interface_permission_list.NetworkInterfacePermissionList"
    ]
    """<p>The network interface permissions.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInterfacePermissionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_interface_permissions" in value:
        import aws_sdk_ec2.types.network_interface_permission_list

        aws_sdk_ec2.types.network_interface_permission_list.serialize_ec2_query(
            value["network_interface_permissions"],
            pairs,
            f"{prefix}.NetworkInterfacePermissions",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInterfacePermissionsResult:
    out: DescribeNetworkInterfacePermissionsResult = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInterfacePermissions") is not None:
        import aws_sdk_ec2.types.network_interface_permission_list

        out["network_interface_permissions"] = (
            aws_sdk_ec2.types.network_interface_permission_list.deserialize_ec2_query(
                el, "NetworkInterfacePermissions"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
