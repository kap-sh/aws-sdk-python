"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PropertyParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.parameter_list


class PropertyParameters(TypedDict, closed=True):
    properties: NotRequired[
        "capo_bedrock_agent_runtime.types.parameter_list.ParameterList"
    ]
    """<p>A list of parameters in the request body.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyParameters) -> dict:
    out: dict = {}
    if "properties" in value:
        import capo_bedrock_agent_runtime.types.parameter_list

        out["properties"] = (
            capo_bedrock_agent_runtime.types.parameter_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> PropertyParameters:
    out: PropertyParameters = {}  # type: ignore[typeddict-item]
    if "properties" in data:
        import capo_bedrock_agent_runtime.types.parameter_list

        out["properties"] = (
            capo_bedrock_agent_runtime.types.parameter_list.deserialize_json(
                data["properties"]
            )
        )
    return out
