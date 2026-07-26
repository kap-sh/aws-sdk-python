"""Generated from Smithy shape ``com.amazonaws.connect#DescribeTrafficDistributionGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.traffic_distribution_group_id_or_arn


class DescribeTrafficDistributionGroupRequest(TypedDict, closed=True):
    traffic_distribution_group_id: "capo_connect.types.traffic_distribution_group_id_or_arn.TrafficDistributionGroupIdOrArn"
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTrafficDistributionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeTrafficDistributionGroupRequest:
    out: DescribeTrafficDistributionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
