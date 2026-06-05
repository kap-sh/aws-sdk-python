"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfacePermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.interface_permission_type
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.string


class CreateNetworkInterfacePermissionRequest(TypedDict):
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    aws_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    aws_service: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services service. Currently not supported.</p>"""
    permission: NotRequired[
        "aws_sdk_ec2.types.interface_permission_type.InterfacePermissionType"
    ]
    """<p>The type of permission to grant.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateNetworkInterfacePermissionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "network_interface_id" in value:
        pairs.append(
            (f"{prefix}.NetworkInterfaceId", str(value["network_interface_id"]))
        )
    if "aws_account_id" in value:
        pairs.append((f"{prefix}.AwsAccountId", str(value["aws_account_id"])))
    if "aws_service" in value:
        pairs.append((f"{prefix}.AwsService", str(value["aws_service"])))
    if "permission" in value:
        import aws_sdk_ec2.types.interface_permission_type

        aws_sdk_ec2.types.interface_permission_type.serialize_ec2_query(
            value["permission"], pairs, f"{prefix}.Permission"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateNetworkInterfacePermissionRequest:
    out: CreateNetworkInterfacePermissionRequest = {}  # type: ignore[typeddict-item]
    child_network_interface_id = el.find("NetworkInterfaceId")
    if child_network_interface_id is not None:
        out["network_interface_id"] = str(child_network_interface_id.text or "")
    child_aws_account_id = el.find("AwsAccountId")
    if child_aws_account_id is not None:
        out["aws_account_id"] = str(child_aws_account_id.text or "")
    child_aws_service = el.find("AwsService")
    if child_aws_service is not None:
        out["aws_service"] = str(child_aws_service.text or "")
    child_permission = el.find("Permission")
    if child_permission is not None:
        import aws_sdk_ec2.types.interface_permission_type

        out["permission"] = (
            aws_sdk_ec2.types.interface_permission_type.deserialize_ec2_query(
                child_permission
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
