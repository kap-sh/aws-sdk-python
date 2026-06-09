"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPrefixListResolverTargetResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_target


class DeleteIpamPrefixListResolverTargetResult(TypedDict):
    ipam_prefix_list_resolver_target: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_target.IpamPrefixListResolverTarget"
    ]
    """<p>Information about the IPAM prefix list resolver target that was deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamPrefixListResolverTargetResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_prefix_list_resolver_target" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_target

        aws_sdk_ec2.types.ipam_prefix_list_resolver_target.serialize_ec2_query(
            value["ipam_prefix_list_resolver_target"],
            pairs,
            f"{prefix}.IpamPrefixListResolverTarget",
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamPrefixListResolverTargetResult:
    out: DeleteIpamPrefixListResolverTargetResult = {}  # type: ignore[typeddict-item]
    child_ipam_prefix_list_resolver_target = el.find("IpamPrefixListResolverTarget")
    if child_ipam_prefix_list_resolver_target is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_target

        out["ipam_prefix_list_resolver_target"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_target.deserialize_ec2_query(
                child_ipam_prefix_list_resolver_target
            )
        )
    return out
