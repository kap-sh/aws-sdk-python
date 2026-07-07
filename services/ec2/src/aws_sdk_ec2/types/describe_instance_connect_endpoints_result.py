"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceConnectEndpointsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_connect_endpoint_set
    import aws_sdk_ec2.types.next_token


class DescribeInstanceConnectEndpointsResult(TypedDict, closed=True):
    instance_connect_endpoints: NotRequired[
        "aws_sdk_ec2.types.instance_connect_endpoint_set.InstanceConnectEndpointSet"
    ]
    """<p>Information about the EC2 Instance Connect Endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceConnectEndpointsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "instance_connect_endpoints" in value:
        import aws_sdk_ec2.types.instance_connect_endpoint_set

        aws_sdk_ec2.types.instance_connect_endpoint_set.serialize_ec2_query(
            value["instance_connect_endpoints"],
            pairs,
            f"{prefix}.InstanceConnectEndpointSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceConnectEndpointsResult:
    out: DescribeInstanceConnectEndpointsResult = {}  # type: ignore[typeddict-item]
    if el.find("InstanceConnectEndpointSet") is not None:
        import aws_sdk_ec2.types.instance_connect_endpoint_set

        out["instance_connect_endpoints"] = (
            aws_sdk_ec2.types.instance_connect_endpoint_set.deserialize_ec2_query(
                el, "InstanceConnectEndpointSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
