"""Generated from Smithy shape ``com.amazonaws.connect#DeleteTrafficDistributionGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.traffic_distribution_group_id_or_arn


class DeleteTrafficDistributionGroupRequest(TypedDict):
    traffic_distribution_group_id: "aws_sdk_connect.types.traffic_distribution_group_id_or_arn.TrafficDistributionGroupIdOrArn"
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN of the traffic distribution group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTrafficDistributionGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteTrafficDistributionGroupRequest:
    out: DeleteTrafficDistributionGroupRequest = {}  # type: ignore[typeddict-item]
    return out
