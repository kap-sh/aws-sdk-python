"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeServiceLinkVirtualInterfacesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_link_virtual_interface_set
    import aws_sdk_ec2.types.string


class DescribeServiceLinkVirtualInterfacesResult(TypedDict):
    service_link_virtual_interfaces: NotRequired[
        "aws_sdk_ec2.types.service_link_virtual_interface_set.ServiceLinkVirtualInterfaceSet"
    ]
    """<p>Describes the service link virtual interfaces.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeServiceLinkVirtualInterfacesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "service_link_virtual_interfaces" in value:
        import aws_sdk_ec2.types.service_link_virtual_interface_set

        aws_sdk_ec2.types.service_link_virtual_interface_set.serialize_ec2_query(
            value["service_link_virtual_interfaces"],
            pairs,
            f"{prefix}.ServiceLinkVirtualInterfaceSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeServiceLinkVirtualInterfacesResult:
    out: DescribeServiceLinkVirtualInterfacesResult = {}  # type: ignore[typeddict-item]
    if el.find("ServiceLinkVirtualInterfaceSet") is not None:
        import aws_sdk_ec2.types.service_link_virtual_interface_set

        out["service_link_virtual_interfaces"] = (
            aws_sdk_ec2.types.service_link_virtual_interface_set.deserialize_ec2_query(
                el, "ServiceLinkVirtualInterfaceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
