"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotInstanceRequestsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_instance_request_list
    import aws_sdk_ec2.types.string


class DescribeSpotInstanceRequestsResult(TypedDict):
    spot_instance_requests: NotRequired[
        "aws_sdk_ec2.types.spot_instance_request_list.SpotInstanceRequestList"
    ]
    """<p>The Spot Instance requests.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotInstanceRequestsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "spot_instance_requests" in value:
        import aws_sdk_ec2.types.spot_instance_request_list

        aws_sdk_ec2.types.spot_instance_request_list.serialize_ec2_query(
            value["spot_instance_requests"], pairs, f"{prefix}.SpotInstanceRequestSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeSpotInstanceRequestsResult:
    out: DescribeSpotInstanceRequestsResult = {}  # type: ignore[typeddict-item]
    if el.find("SpotInstanceRequestSet") is not None:
        import aws_sdk_ec2.types.spot_instance_request_list

        out["spot_instance_requests"] = (
            aws_sdk_ec2.types.spot_instance_request_list.deserialize_ec2_query(
                el, "SpotInstanceRequestSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
