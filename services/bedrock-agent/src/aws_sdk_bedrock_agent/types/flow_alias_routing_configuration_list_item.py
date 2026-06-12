"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowAliasRoutingConfigurationListItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.version


class FlowAliasRoutingConfigurationListItem(TypedDict):
    flow_version: NotRequired["aws_sdk_bedrock_agent.types.version.Version"]
    """<p>The version that the alias maps to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowAliasRoutingConfigurationListItem) -> dict:
    out: dict = {}
    if "flow_version" in value:
        out["flowVersion"] = value["flow_version"]
    return out


def deserialize_json(data: dict) -> FlowAliasRoutingConfigurationListItem:
    out: FlowAliasRoutingConfigurationListItem = {}  # type: ignore[typeddict-item]
    if "flowVersion" in data:
        out["flow_version"] = data["flowVersion"]
    return out
