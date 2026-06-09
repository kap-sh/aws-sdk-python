"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondaryNetworksResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_network_list
    import aws_sdk_ec2.types.string


class DescribeSecondaryNetworksResult(TypedDict):
    secondary_networks: NotRequired[
        "aws_sdk_ec2.types.secondary_network_list.SecondaryNetworkList"
    ]
    """<p>Information about the secondary networks.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecondaryNetworksResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_networks" in value:
        import aws_sdk_ec2.types.secondary_network_list

        aws_sdk_ec2.types.secondary_network_list.serialize_ec2_query(
            value["secondary_networks"], pairs, f"{prefix}.SecondaryNetworkSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSecondaryNetworksResult:
    out: DescribeSecondaryNetworksResult = {}  # type: ignore[typeddict-item]
    if el.find("SecondaryNetworkSet") is not None:
        import aws_sdk_ec2.types.secondary_network_list

        out["secondary_networks"] = (
            aws_sdk_ec2.types.secondary_network_list.deserialize_ec2_query(
                el, "SecondaryNetworkSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
