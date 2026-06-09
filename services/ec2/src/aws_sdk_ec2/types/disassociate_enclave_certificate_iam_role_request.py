"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateEnclaveCertificateIamRoleRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.certificate_id
    import aws_sdk_ec2.types.role_id


class DisassociateEnclaveCertificateIamRoleRequest(TypedDict):
    certificate_arn: NotRequired["aws_sdk_ec2.types.certificate_id.CertificateId"]
    """<p>The ARN of the ACM certificate from which to disassociate the IAM role.</p>"""
    role_arn: NotRequired["aws_sdk_ec2.types.role_id.RoleId"]
    """<p>The ARN of the IAM role to disassociate.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DisassociateEnclaveCertificateIamRoleRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "certificate_arn" in value:
        pairs.append((f"{prefix}.CertificateArn", str(value["certificate_arn"])))
    if "role_arn" in value:
        pairs.append((f"{prefix}.RoleArn", str(value["role_arn"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DisassociateEnclaveCertificateIamRoleRequest:
    out: DisassociateEnclaveCertificateIamRoleRequest = {}  # type: ignore[typeddict-item]
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
