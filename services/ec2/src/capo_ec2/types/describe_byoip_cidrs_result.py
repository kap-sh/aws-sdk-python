"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeByoipCidrsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.byoip_cidr_set
    import capo_ec2.types.string


class DescribeByoipCidrsResult(TypedDict, closed=True):
    byoip_cidrs: NotRequired["capo_ec2.types.byoip_cidr_set.ByoipCidrSet"]
    """<p>Information about your address ranges.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeByoipCidrsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "byoip_cidrs" in value:
        import capo_ec2.types.byoip_cidr_set

        capo_ec2.types.byoip_cidr_set.serialize_ec2_query(
            value["byoip_cidrs"], pairs, f"{key_prefix}ByoipCidrSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeByoipCidrsResult:
    out: DescribeByoipCidrsResult = {}  # type: ignore[typeddict-item]
    if el.find("ByoipCidrSet") is not None:
        import capo_ec2.types.byoip_cidr_set

        out["byoip_cidrs"] = capo_ec2.types.byoip_cidr_set.deserialize_ec2_query(
            el, "ByoipCidrSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
