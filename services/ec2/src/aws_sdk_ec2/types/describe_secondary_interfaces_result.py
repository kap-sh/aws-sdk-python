"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondaryInterfacesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_interface_list
    import aws_sdk_ec2.types.string


class DescribeSecondaryInterfacesResult(TypedDict, closed=True):
    secondary_interfaces: NotRequired[
        "aws_sdk_ec2.types.secondary_interface_list.SecondaryInterfaceList"
    ]
    """<p>Information about the secondary interfaces.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecondaryInterfacesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_interfaces" in value:
        import aws_sdk_ec2.types.secondary_interface_list

        aws_sdk_ec2.types.secondary_interface_list.serialize_ec2_query(
            value["secondary_interfaces"], pairs, f"{prefix}.SecondaryInterfaceSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSecondaryInterfacesResult:
    out: DescribeSecondaryInterfacesResult = {}  # type: ignore[typeddict-item]
    if el.find("SecondaryInterfaceSet") is not None:
        import aws_sdk_ec2.types.secondary_interface_list

        out["secondary_interfaces"] = (
            aws_sdk_ec2.types.secondary_interface_list.deserialize_ec2_query(
                el, "SecondaryInterfaceSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
