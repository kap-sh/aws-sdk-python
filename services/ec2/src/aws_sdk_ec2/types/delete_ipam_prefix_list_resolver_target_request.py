"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPrefixListResolverTargetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id


class DeleteIpamPrefixListResolverTargetRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    ipam_prefix_list_resolver_target_id: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target_id.IpamPrefixListResolverTargetId"
    ]
    """<p>The ID of the IPAM prefix list resolver target to delete.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamPrefixListResolverTargetRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "ipam_prefix_list_resolver_target_id" in value:
        pairs.append(
            (
                f"{prefix}.IpamPrefixListResolverTargetId",
                str(value["ipam_prefix_list_resolver_target_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamPrefixListResolverTargetRequest:
    out: DeleteIpamPrefixListResolverTargetRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_ipam_prefix_list_resolver_target_id = el.find(
        "IpamPrefixListResolverTargetId"
    )
    if child_ipam_prefix_list_resolver_target_id is not None:
        out["ipam_prefix_list_resolver_target_id"] = str(
            child_ipam_prefix_list_resolver_target_id.text or ""
        )
    return out
