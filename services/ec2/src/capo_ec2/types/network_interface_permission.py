"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.interface_permission_type
    import capo_ec2.types.network_interface_permission_state
    import capo_ec2.types.string


class NetworkInterfacePermission(TypedDict, closed=True):
    network_interface_permission_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface permission.</p>"""
    network_interface_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    aws_account_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    aws_service: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services service.</p>"""
    permission: NotRequired[
        "capo_ec2.types.interface_permission_type.InterfacePermissionType"
    ]
    """<p>The type of permission.</p>"""
    permission_state: NotRequired[
        "capo_ec2.types.network_interface_permission_state.NetworkInterfacePermissionState"
    ]
    """<p>Information about the state of the permission.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfacePermission, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "network_interface_permission_id" in value:
        pairs.append(
            (
                f"{key_prefix}NetworkInterfacePermissionId",
                str(value["network_interface_permission_id"]),
            )
        )
    if "network_interface_id" in value:
        pairs.append(
            (f"{key_prefix}NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "aws_account_id" in value:
        pairs.append((f"{key_prefix}AwsAccountId", str(value["aws_account_id"])))
    if "aws_service" in value:
        pairs.append((f"{key_prefix}AwsService", str(value["aws_service"])))
    if "permission" in value:
        import capo_ec2.types.interface_permission_type

        capo_ec2.types.interface_permission_type.serialize_ec2_query(
            value["permission"], pairs, f"{key_prefix}Permission"
        )
    if "permission_state" in value:
        import capo_ec2.types.network_interface_permission_state

        capo_ec2.types.network_interface_permission_state.serialize_ec2_query(
            value["permission_state"], pairs, f"{key_prefix}PermissionState"
        )


def deserialize_ec2_query(el: Element) -> NetworkInterfacePermission:
    out: NetworkInterfacePermission = {}  # type: ignore[typeddict-item]
    child_network_interface_permission_id = el.find("networkInterfacePermissionId")
    if child_network_interface_permission_id is not None:
        out["network_interface_permission_id"] = str(
            child_network_interface_permission_id.text or ""
        )
    child_network_interface_id = el.find("networkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_aws_account_id = el.find("awsAccountId")
    if child_aws_account_id is not None:
        out["aws_account_id"] = str(child_aws_account_id.text or "")
    child_aws_service = el.find("awsService")
    if child_aws_service is not None:
        out["aws_service"] = str(child_aws_service.text or "")
    child_permission = el.find("permission")
    if child_permission is not None:
        import capo_ec2.types.interface_permission_type

        out["permission"] = (
            capo_ec2.types.interface_permission_type.deserialize_ec2_query(
                child_permission
            )
        )
    child_permission_state = el.find("permissionState")
    if child_permission_state is not None:
        import capo_ec2.types.network_interface_permission_state

        out["permission_state"] = (
            capo_ec2.types.network_interface_permission_state.deserialize_ec2_query(
                child_permission_state
            )
        )
    return out
