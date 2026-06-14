"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#TrafficSplitEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_reference
    import aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_map


class TrafficSplitEntry(TypedDict):
    name: "str"
    """<p>The name of this traffic split variant.</p>"""
    weight: "int"
    """<p>The percentage of traffic to route to this variant. Weights across all entries must sum to 100.</p>"""
    configuration_bundle: "aws_sdk_bedrock_agentcore_control.types.configuration_bundle_reference.ConfigurationBundleReference"
    """<p>The configuration bundle reference for this variant.</p>"""
    description: NotRequired["str"]
    """<p>The description of this traffic split variant.</p>"""
    metadata: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_map.TrafficSplitMetadataMap"
    ]
    """<p>Key-value metadata associated with this traffic split variant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficSplitEntry) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["weight"] = value["weight"]
    import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_reference

    out["configurationBundle"] = (
        aws_sdk_bedrock_agentcore_control.types.configuration_bundle_reference.serialize_json(
            value["configuration_bundle"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    if "metadata" in value:
        import aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_map

        out["metadata"] = (
            aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_map.serialize_json(
                value["metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> TrafficSplitEntry:
    out: TrafficSplitEntry = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("TrafficSplitEntry.name required")
    if "weight" in data:
        out["weight"] = data["weight"]
    else:
        raise DeserializationError("TrafficSplitEntry.weight required")
    if "configurationBundle" in data:
        import aws_sdk_bedrock_agentcore_control.types.configuration_bundle_reference

        out["configuration_bundle"] = (
            aws_sdk_bedrock_agentcore_control.types.configuration_bundle_reference.deserialize_json(
                data["configurationBundle"]
            )
        )
    else:
        raise DeserializationError("TrafficSplitEntry.configuration_bundle required")
    if "description" in data:
        out["description"] = data["description"]
    if "metadata" in data:
        import aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_map

        out["metadata"] = (
            aws_sdk_bedrock_agentcore_control.types.traffic_split_metadata_map.deserialize_json(
                data["metadata"]
            )
        )
    return out
