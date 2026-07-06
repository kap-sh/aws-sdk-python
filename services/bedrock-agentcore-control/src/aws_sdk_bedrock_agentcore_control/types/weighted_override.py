"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#WeightedOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_entries


class WeightedOverride(TypedDict, closed=True):
    traffic_split: "aws_sdk_bedrock_agentcore_control.types.traffic_split_entries.TrafficSplitEntries"
    """<p>The traffic split entries defining how traffic is distributed between configuration bundle versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedOverride) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_entries

    out["trafficSplit"] = (
        aws_sdk_bedrock_agentcore_control.types.traffic_split_entries.serialize_json(
            value["traffic_split"]
        )
    )
    return out


def deserialize_json(data: dict) -> WeightedOverride:
    out: WeightedOverride = {}  # type: ignore[typeddict-item]
    if "trafficSplit" in data:
        import aws_sdk_bedrock_agentcore_control.types.traffic_split_entries

        out["traffic_split"] = (
            aws_sdk_bedrock_agentcore_control.types.traffic_split_entries.deserialize_json(
                data["trafficSplit"]
            )
        )
    else:
        raise DeserializationError("WeightedOverride.traffic_split required")
    return out
