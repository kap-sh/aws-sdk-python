"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSubnetsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.subnet_list


class DescribeSubnetsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    subnets: NotRequired["aws_sdk_ec2.types.subnet_list.SubnetList"]
    """<p>Information about the subnets.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSubnetsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "subnets" in value:
        import aws_sdk_ec2.types.subnet_list

        aws_sdk_ec2.types.subnet_list.serialize_ec2_query(
            value["subnets"], pairs, f"{prefix}.SubnetSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeSubnetsResult:
    out: DescribeSubnetsResult = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("SubnetSet") is not None:
        import aws_sdk_ec2.types.subnet_list

        out["subnets"] = aws_sdk_ec2.types.subnet_list.deserialize_ec2_query(
            el, "SubnetSet"
        )
    return out
