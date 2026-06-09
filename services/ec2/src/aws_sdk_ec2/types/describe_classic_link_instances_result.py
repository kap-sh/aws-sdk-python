"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeClassicLinkInstancesResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_link_instance_list
    import aws_sdk_ec2.types.string


class DescribeClassicLinkInstancesResult(TypedDict):
    instances: NotRequired[
        "aws_sdk_ec2.types.classic_link_instance_list.ClassicLinkInstanceList"
    ]
    """<p>Information about one or more linked EC2-Classic instances.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeClassicLinkInstancesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "instances" in value:
        import aws_sdk_ec2.types.classic_link_instance_list

        aws_sdk_ec2.types.classic_link_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{prefix}.InstancesSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeClassicLinkInstancesResult:
    out: DescribeClassicLinkInstancesResult = {}  # type: ignore[typeddict-item]
    if el.find("InstancesSet") is not None:
        import aws_sdk_ec2.types.classic_link_instance_list

        out["instances"] = (
            aws_sdk_ec2.types.classic_link_instance_list.deserialize_ec2_query(
                el, "InstancesSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
