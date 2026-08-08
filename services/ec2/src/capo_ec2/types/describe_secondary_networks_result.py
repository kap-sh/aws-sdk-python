"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondaryNetworksResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_network_list
    import capo_ec2.types.string


class DescribeSecondaryNetworksResult(TypedDict, closed=True):
    secondary_networks: NotRequired[
        "capo_ec2.types.secondary_network_list.SecondaryNetworkList"
    ]
    """<p>Information about the secondary networks.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecondaryNetworksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "secondary_networks" in value:
        import capo_ec2.types.secondary_network_list

        capo_ec2.types.secondary_network_list.serialize_ec2_query(
            value["secondary_networks"], pairs, f"{key_prefix}SecondaryNetworkSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSecondaryNetworksResult:
    out: DescribeSecondaryNetworksResult = {}  # type: ignore[typeddict-item]
    if el.find("secondaryNetworkSet") is not None:
        import capo_ec2.types.secondary_network_list

        out["secondary_networks"] = (
            capo_ec2.types.secondary_network_list.deserialize_ec2_query(
                el, "secondaryNetworkSet"
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
