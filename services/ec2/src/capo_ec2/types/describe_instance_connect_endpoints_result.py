"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceConnectEndpointsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_connect_endpoint_set
    import capo_ec2.types.next_token


class DescribeInstanceConnectEndpointsResult(TypedDict, closed=True):
    instance_connect_endpoints: NotRequired[
        "capo_ec2.types.instance_connect_endpoint_set.InstanceConnectEndpointSet"
    ]
    """<p>Information about the EC2 Instance Connect Endpoints.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceConnectEndpointsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_connect_endpoints" in value:
        import capo_ec2.types.instance_connect_endpoint_set

        capo_ec2.types.instance_connect_endpoint_set.serialize_ec2_query(
            value["instance_connect_endpoints"],
            pairs,
            f"{key_prefix}InstanceConnectEndpointSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceConnectEndpointsResult:
    out: DescribeInstanceConnectEndpointsResult = {}  # type: ignore[typeddict-item]
    child_instance_connect_endpoints = el.find("instanceConnectEndpointSet")
    if child_instance_connect_endpoints is not None:
        import capo_ec2.types.instance_connect_endpoint_set

        out["instance_connect_endpoints"] = (
            capo_ec2.types.instance_connect_endpoint_set.deserialize_ec2_query(
                child_instance_connect_endpoints
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
