"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WeightedRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entries


class WeightedRoute(TypedDict, closed=True):
    traffic_split: "aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entries.TargetTrafficSplitEntries"
    """<p>The traffic split entries defining how traffic is distributed between targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedRoute) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entries

    out["trafficSplit"] = (
        aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entries.serialize_json(
            value["traffic_split"]
        )
    )
    return out


def deserialize_json(data: dict) -> WeightedRoute:
    out: WeightedRoute = {}  # type: ignore[typeddict-item]
    if "trafficSplit" in data:
        import aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entries

        out["traffic_split"] = (
            aws_sdk_bedrock_agentcore_control.types.target_traffic_split_entries.deserialize_json(
                data["trafficSplit"]
            )
        )
    else:
        raise DeserializationError("WeightedRoute.traffic_split required")
    return out
