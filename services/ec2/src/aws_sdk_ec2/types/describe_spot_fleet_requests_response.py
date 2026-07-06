"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotFleetRequestsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.spot_fleet_request_config_set
    import aws_sdk_ec2.types.string


class DescribeSpotFleetRequestsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    spot_fleet_request_configs: NotRequired[
        "aws_sdk_ec2.types.spot_fleet_request_config_set.SpotFleetRequestConfigSet"
    ]
    """<p>Information about the configuration of your Spot Fleet.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotFleetRequestsResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "spot_fleet_request_configs" in value:
        import aws_sdk_ec2.types.spot_fleet_request_config_set

        aws_sdk_ec2.types.spot_fleet_request_config_set.serialize_ec2_query(
            value["spot_fleet_request_configs"],
            pairs,
            f"{prefix}.SpotFleetRequestConfigSet",
        )


def deserialize_ec2_query(el: Element) -> DescribeSpotFleetRequestsResponse:
    out: DescribeSpotFleetRequestsResponse = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    if el.find("SpotFleetRequestConfigSet") is not None:
        import aws_sdk_ec2.types.spot_fleet_request_config_set

        out["spot_fleet_request_configs"] = (
            aws_sdk_ec2.types.spot_fleet_request_config_set.deserialize_ec2_query(
                el, "SpotFleetRequestConfigSet"
            )
        )
    return out
