"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamPrefixListResolverResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver


class DeleteIpamPrefixListResolverResult(TypedDict):
    ipam_prefix_list_resolver: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver.IpamPrefixListResolver"
    ]
    """<p>Information about the IPAM prefix list resolver that was deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteIpamPrefixListResolverResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_prefix_list_resolver" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver

        aws_sdk_ec2.types.ipam_prefix_list_resolver.serialize_ec2_query(
            value["ipam_prefix_list_resolver"],
            pairs,
            f"{prefix}.IpamPrefixListResolver",
        )


def deserialize_ec2_query(el: Element) -> DeleteIpamPrefixListResolverResult:
    out: DeleteIpamPrefixListResolverResult = {}  # type: ignore[typeddict-item]
    child_ipam_prefix_list_resolver = el.find("IpamPrefixListResolver")
    if child_ipam_prefix_list_resolver is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver

        out["ipam_prefix_list_resolver"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver.deserialize_ec2_query(
                child_ipam_prefix_list_resolver
            )
        )
    return out
