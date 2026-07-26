"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeNetworkInterfacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.network_interface_list
    import capo_ec2.types.string


class DescribeNetworkInterfacesResult(TypedDict, closed=True):
    network_interfaces: NotRequired[
        "capo_ec2.types.network_interface_list.NetworkInterfaceList"
    ]
    """<p>Information about the network interfaces.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeNetworkInterfacesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "network_interfaces" in value:
        import capo_ec2.types.network_interface_list

        capo_ec2.types.network_interface_list.serialize_ec2_query(
            value["network_interfaces"], pairs, f"{prefix}.NetworkInterfaceSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeNetworkInterfacesResult:
    out: DescribeNetworkInterfacesResult = {}  # type: ignore[typeddict-item]
    if el.find("NetworkInterfaceSet") is not None:
        import capo_ec2.types.network_interface_list

        out["network_interfaces"] = (
            capo_ec2.types.network_interface_list.deserialize_ec2_query(
                el, "NetworkInterfaceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
