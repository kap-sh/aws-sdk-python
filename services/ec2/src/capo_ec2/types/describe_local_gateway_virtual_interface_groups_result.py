"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayVirtualInterfaceGroupsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_virtual_interface_group_set
    import capo_ec2.types.string


class DescribeLocalGatewayVirtualInterfaceGroupsResult(TypedDict, closed=True):
    local_gateway_virtual_interface_groups: NotRequired[
        "capo_ec2.types.local_gateway_virtual_interface_group_set.LocalGatewayVirtualInterfaceGroupSet"
    ]
    """<p>The virtual interface groups.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewayVirtualInterfaceGroupsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_virtual_interface_groups" in value:
        import capo_ec2.types.local_gateway_virtual_interface_group_set

        capo_ec2.types.local_gateway_virtual_interface_group_set.serialize_ec2_query(
            value["local_gateway_virtual_interface_groups"],
            pairs,
            f"{key_prefix}LocalGatewayVirtualInterfaceGroupSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeLocalGatewayVirtualInterfaceGroupsResult:
    out: DescribeLocalGatewayVirtualInterfaceGroupsResult = {}  # type: ignore[typeddict-item]
    if el.find("LocalGatewayVirtualInterfaceGroupSet") is not None:
        import capo_ec2.types.local_gateway_virtual_interface_group_set

        out["local_gateway_virtual_interface_groups"] = (
            capo_ec2.types.local_gateway_virtual_interface_group_set.deserialize_ec2_query(
                el, "LocalGatewayVirtualInterfaceGroupSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
