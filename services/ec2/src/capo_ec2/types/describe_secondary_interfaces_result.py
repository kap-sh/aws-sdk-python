"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondaryInterfacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_interface_list
    import capo_ec2.types.string


class DescribeSecondaryInterfacesResult(TypedDict, closed=True):
    secondary_interfaces: NotRequired[
        "capo_ec2.types.secondary_interface_list.SecondaryInterfaceList"
    ]
    """<p>Information about the secondary interfaces.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecondaryInterfacesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "secondary_interfaces" in value:
        import capo_ec2.types.secondary_interface_list

        capo_ec2.types.secondary_interface_list.serialize_ec2_query(
            value["secondary_interfaces"], pairs, f"{key_prefix}SecondaryInterfaceSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSecondaryInterfacesResult:
    out: DescribeSecondaryInterfacesResult = {}  # type: ignore[typeddict-item]
    child_secondary_interfaces = el.find("secondaryInterfaceSet")
    if child_secondary_interfaces is not None:
        import capo_ec2.types.secondary_interface_list

        out["secondary_interfaces"] = (
            capo_ec2.types.secondary_interface_list.deserialize_ec2_query(
                child_secondary_interfaces
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
