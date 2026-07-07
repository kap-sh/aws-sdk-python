"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecondarySubnetsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_subnet_list
    import aws_sdk_ec2.types.string


class DescribeSecondarySubnetsResult(TypedDict, closed=True):
    secondary_subnets: NotRequired[
        "aws_sdk_ec2.types.secondary_subnet_list.SecondarySubnetList"
    ]
    """<p>Information about the secondary subnets.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSecondarySubnetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "secondary_subnets" in value:
        import aws_sdk_ec2.types.secondary_subnet_list

        aws_sdk_ec2.types.secondary_subnet_list.serialize_ec2_query(
            value["secondary_subnets"], pairs, f"{prefix}.SecondarySubnetSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSecondarySubnetsResult:
    out: DescribeSecondarySubnetsResult = {}  # type: ignore[typeddict-item]
    if el.find("SecondarySubnetSet") is not None:
        import aws_sdk_ec2.types.secondary_subnet_list

        out["secondary_subnets"] = (
            aws_sdk_ec2.types.secondary_subnet_list.deserialize_ec2_query(
                el, "SecondarySubnetSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
