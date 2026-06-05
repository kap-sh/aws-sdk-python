"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcBlockPublicAccessExclusionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.vpc_block_public_access_exclusion_id


class DeleteVpcBlockPublicAccessExclusionRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    exclusion_id: NotRequired[
        "aws_sdk_ec2.types.vpc_block_public_access_exclusion_id.VpcBlockPublicAccessExclusionId"
    ]
    """<p>The ID of the exclusion.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteVpcBlockPublicAccessExclusionRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "exclusion_id" in value:
        pairs.append((f"{prefix}.ExclusionId", str(value["exclusion_id"])))


def deserialize_ec2_query(el: Element) -> DeleteVpcBlockPublicAccessExclusionRequest:
    out: DeleteVpcBlockPublicAccessExclusionRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_exclusion_id = el.find("ExclusionId")
    if child_exclusion_id is not None:
        out["exclusion_id"] = str(child_exclusion_id.text or "")
    return out
