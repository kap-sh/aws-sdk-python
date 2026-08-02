"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeDhcpOptionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dhcp_options_list
    import capo_ec2.types.string


class DescribeDhcpOptionsResult(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    dhcp_options: NotRequired["capo_ec2.types.dhcp_options_list.DhcpOptionsList"]
    """<p>Information about the DHCP options sets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeDhcpOptionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "dhcp_options" in value:
        import capo_ec2.types.dhcp_options_list

        capo_ec2.types.dhcp_options_list.serialize_ec2_query(
            value["dhcp_options"], pairs, f"{key_prefix}DhcpOptionsSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeDhcpOptionsResult:
    out: DescribeDhcpOptionsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("DhcpOptionsSet") is not None:
        import capo_ec2.types.dhcp_options_list

        out["dhcp_options"] = capo_ec2.types.dhcp_options_list.deserialize_ec2_query(
            el, "DhcpOptionsSet"
        )
    return out
