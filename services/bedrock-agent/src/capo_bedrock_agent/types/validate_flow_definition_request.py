"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ValidateFlowDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_definition


class ValidateFlowDefinitionRequest(TypedDict, closed=True):
    definition: "capo_bedrock_agent.types.flow_definition.FlowDefinition"
    """<p>The definition of a flow to validate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateFlowDefinitionRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.flow_definition

    out["definition"] = capo_bedrock_agent.types.flow_definition.serialize_json(
        value["definition"]
    )
    return out


def deserialize_json(data: dict) -> ValidateFlowDefinitionRequest:
    out: ValidateFlowDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "definition" in data:
        import capo_bedrock_agent.types.flow_definition

        out["definition"] = capo_bedrock_agent.types.flow_definition.deserialize_json(
            data["definition"]
        )
    else:
        raise DeserializationError("ValidateFlowDefinitionRequest.definition required")
    return out
