"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPrefixListResolverVersionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_set
    import aws_sdk_ec2.types.next_token


class GetIpamPrefixListResolverVersionsResult(TypedDict):
    ipam_prefix_list_resolver_versions: NotRequired[
        "aws_sdk_ec2.types.ipam_prefix_list_resolver_version_set.IpamPrefixListResolverVersionSet"
    ]
    """<p>Information about the IPAM prefix list resolver versions.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetIpamPrefixListResolverVersionsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "ipam_prefix_list_resolver_versions" in value:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_set

        aws_sdk_ec2.types.ipam_prefix_list_resolver_version_set.serialize_ec2_query(
            value["ipam_prefix_list_resolver_versions"],
            pairs,
            f"{prefix}.IpamPrefixListResolverVersionSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetIpamPrefixListResolverVersionsResult:
    out: GetIpamPrefixListResolverVersionsResult = {}  # type: ignore[typeddict-item]
    if el.find("IpamPrefixListResolverVersionSet") is not None:
        import aws_sdk_ec2.types.ipam_prefix_list_resolver_version_set

        out["ipam_prefix_list_resolver_versions"] = (
            aws_sdk_ec2.types.ipam_prefix_list_resolver_version_set.deserialize_ec2_query(
                el, "IpamPrefixListResolverVersionSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
