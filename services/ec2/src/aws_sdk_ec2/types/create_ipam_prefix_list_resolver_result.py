"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPrefixListResolverResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver


class CreateIpamPrefixListResolverResult(TypedDict, closed=True):
    ipam_prefix_list_resolver: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver.IpamPrefixListResolver"
    ]
    """<p>Information about the IPAM prefix list resolver that was created.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateIpamPrefixListResolverResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "ipam_prefix_list_resolver" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver

        aws_sdk_ec2.types.ipam_prefix_list_resolver.serialize_ec2_query(
            value["ipam_prefix_list_resolver"],
            pairs,
            f"{prefix}.IpamPrefixListResolver",
        )


def deserialize_ec2_query(el: Element) -> CreateIpamPrefixListResolverResult:
    out: CreateIpamPrefixListResolverResult = {}  # type: ignore[typeddict-item]
    child_ipam_prefix_list_resolver = el.find("IpamPrefixListResolver")
    if child_ipam_prefix_list_resolver is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver

        out["ipam_prefix_list_resolver"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver.deserialize_ec2_query(
                child_ipam_prefix_list_resolver
            )
        )
    return out
