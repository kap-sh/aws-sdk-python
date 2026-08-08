"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamByoasnResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.byoasn_set
    import capo_ec2.types.string


class DescribeIpamByoasnResult(TypedDict, closed=True):
    byoasns: NotRequired["capo_ec2.types.byoasn_set.ByoasnSet"]
    """<p>ASN and BYOIP CIDR associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeIpamByoasnResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "byoasns" in value:
        import capo_ec2.types.byoasn_set

        capo_ec2.types.byoasn_set.serialize_ec2_query(
            value["byoasns"], pairs, f"{key_prefix}ByoasnSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeIpamByoasnResult:
    out: DescribeIpamByoasnResult = {}  # type: ignore[typeddict-item]
    if el.find("byoasnSet") is not None:
        import capo_ec2.types.byoasn_set

        out["byoasns"] = capo_ec2.types.byoasn_set.deserialize_ec2_query(
            el, "byoasnSet"
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
