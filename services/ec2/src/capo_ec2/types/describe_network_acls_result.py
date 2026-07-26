"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkAclsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_acl_list
    import capo_ec2.types.string


class DescribeNetworkAclsResult(TypedDict, closed=True):
    network_acls: NotRequired["capo_ec2.types.network_acl_list.NetworkAclList"]
    """<p>Information about the network ACLs.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkAclsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_acls" in value:
        import capo_ec2.types.network_acl_list

        capo_ec2.types.network_acl_list.serialize_ec2_query(
            value["network_acls"], pairs, f"{prefix}.NetworkAclSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkAclsResult:
    out: DescribeNetworkAclsResult = {}  # type: ignore[typeddict-item]
    if el.find("NetworkAclSet") is not None:
        import capo_ec2.types.network_acl_list

        out["network_acls"] = capo_ec2.types.network_acl_list.deserialize_ec2_query(
            el, "NetworkAclSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
