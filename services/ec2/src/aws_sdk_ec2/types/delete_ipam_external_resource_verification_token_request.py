"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamExternalResourceVerificationTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_external_resource_verification_token_id


class DeleteIpamExternalResourceVerificationTokenRequest(TypedDict, closed=True):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_external_resource_verification_token_id: NotRequired[
        "aws_sdk_ec2.types.ipam_external_resource_verification_token_id.IpamExternalResourceVerificationTokenId"
    ]
    """<p>The token ID.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamExternalResourceVerificationTokenRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_external_resource_verification_token_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamExternalResourceVerificationTokenId",
                str(value["ipam_external_resource_verification_token_id"]),
            )
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteIpamExternalResourceVerificationTokenRequest:
    out: DeleteIpamExternalResourceVerificationTokenRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_external_resource_verification_token_id = el.find(
        "IpamExternalResourceVerificationTokenId"
    )
    if child_ipam_external_resource_verification_token_id is not None:
        out["ipam_external_resource_verification_token_id"] = str(
            child_ipam_external_resource_verification_token_id.text or ""
        )
    return out
