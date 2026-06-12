"""Generated from Smithy shape ``com.amazonaws.connect#CreateTrafficDistributionGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.traffic_distribution_group_arn
    import aws_sdk_connect.types.traffic_distribution_group_id


class CreateTrafficDistributionGroupResponse(TypedDict):
    id: NotRequired[
        "aws_sdk_connect.types.traffic_distribution_group_id.TrafficDistributionGroupId"
    ]
    """<p>The identifier of the traffic distribution group. This can be the ID or the ARN of the traffic distribution group.</p>"""
    arn: NotRequired[
        "aws_sdk_connect.types.traffic_distribution_group_arn.TrafficDistributionGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the traffic distribution group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTrafficDistributionGroupResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateTrafficDistributionGroupResponse:
    out: CreateTrafficDistributionGroupResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
