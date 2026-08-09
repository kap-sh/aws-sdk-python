"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_set
    import capo_ec2.types.next_token


class DescribeIpamsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipams: NotRequired["capo_ec2.types.ipam_set.IpamSet"]
    """<p>Information about the IPAMs.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "ipams" in value:
        import capo_ec2.types.ipam_set

        capo_ec2.types.ipam_set.serialize_ec2_query(
            value["ipams"], pairs, f"{key_prefix}IpamSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeIpamsResult:
    out: DescribeIpamsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_ipams = el.find("ipamSet")
    if child_ipams is not None:
        import capo_ec2.types.ipam_set

        out["ipams"] = capo_ec2.types.ipam_set.deserialize_ec2_query(child_ipams)
    return out
