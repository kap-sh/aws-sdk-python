"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UnknownConnectionSourceFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.flow_connection_name


class UnknownConnectionSourceFlowValidationDetails(TypedDict, closed=True):
    connection: "capo_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection with the unknown source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnknownConnectionSourceFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> UnknownConnectionSourceFlowValidationDetails:
    out: UnknownConnectionSourceFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    else:
        raise DeserializationError(
            "UnknownConnectionSourceFlowValidationDetails.connection required"
        )
    return out
