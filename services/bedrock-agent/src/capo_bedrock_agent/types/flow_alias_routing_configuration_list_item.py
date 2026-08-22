"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowAliasRoutingConfigurationListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.version


class FlowAliasRoutingConfigurationListItem(TypedDict, closed=True):
    flow_version: NotRequired["capo_bedrock_agent.types.version.Version"]
    """<p>The version that the alias maps to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowAliasRoutingConfigurationListItem) -> dict:
    out: dict = {}
    if "flow_version" in value:
        out["flowVersion"] = value["flow_version"]
    return out


def deserialize_json(data: dict) -> FlowAliasRoutingConfigurationListItem:
    out: FlowAliasRoutingConfigurationListItem = {}  # type: ignore[typeddict-item]
    if data.get("flowVersion") is not None:
        out["flow_version"] = data["flowVersion"]
    return out
