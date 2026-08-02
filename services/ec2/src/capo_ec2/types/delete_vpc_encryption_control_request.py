"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcEncryptionControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.vpc_encryption_control_id


class DeleteVpcEncryptionControlRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    vpc_encryption_control_id: NotRequired[
        "capo_ec2.types.vpc_encryption_control_id.VpcEncryptionControlId"
    ]
    """<p>The ID of the VPC Encryption Control resource to delete.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteVpcEncryptionControlRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "vpc_encryption_control_id" in value:
        pairs.append(
            (
                f"{key_prefix}VpcEncryptionControlId",
                str(value["vpc_encryption_control_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteVpcEncryptionControlRequest:
    out: DeleteVpcEncryptionControlRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_vpc_encryption_control_id = el.find("VpcEncryptionControlId")
    if child_vpc_encryption_control_id is not None:
        out["vpc_encryption_control_id"] = str(
            child_vpc_encryption_control_id.text or ""
        )
    return out
