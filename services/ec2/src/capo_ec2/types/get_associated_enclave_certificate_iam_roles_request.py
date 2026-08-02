"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedEnclaveCertificateIamRolesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.certificate_id


class GetAssociatedEnclaveCertificateIamRolesRequest(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_ec2.types.certificate_id.CertificateId"]
    """<p>The ARN of the ACM certificate for which to view the associated IAM roles, encryption keys, and Amazon S3 object information.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetAssociatedEnclaveCertificateIamRolesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "certificate_arn" in value:
        pairs.append((f"{key_prefix}CertificateArn", str(value["certificate_arn"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(
    el: Element,
) -> GetAssociatedEnclaveCertificateIamRolesRequest:
    out: GetAssociatedEnclaveCertificateIamRolesRequest = {}  # type: ignore[typeddict-item]
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
