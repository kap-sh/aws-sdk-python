"""Generated from Smithy shape ``com.amazonaws.connect#DescribeTrafficDistributionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.traffic_distribution_group


class DescribeTrafficDistributionGroupResponse(TypedDict, closed=True):
    traffic_distribution_group: NotRequired[
        "capo_connect.types.traffic_distribution_group.TrafficDistributionGroup"
    ]
    """<p>Information about the traffic distribution group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTrafficDistributionGroupResponse) -> dict:
    out: dict = {}
    if "traffic_distribution_group" in value:
        import capo_connect.types.traffic_distribution_group

        out["TrafficDistributionGroup"] = (
            capo_connect.types.traffic_distribution_group.serialize_json(
                value["traffic_distribution_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeTrafficDistributionGroupResponse:
    out: DescribeTrafficDistributionGroupResponse = {}  # type: ignore[typeddict-item]
    if "TrafficDistributionGroup" in data:
        import capo_connect.types.traffic_distribution_group

        out["traffic_distribution_group"] = (
            capo_connect.types.traffic_distribution_group.deserialize_json(
                data["TrafficDistributionGroup"]
            )
        )
    return out
