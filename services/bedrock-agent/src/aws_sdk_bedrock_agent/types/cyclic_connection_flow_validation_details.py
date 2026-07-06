"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CyclicConnectionFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_connection_name


class CyclicConnectionFlowValidationDetails(TypedDict, closed=True):
    connection: "aws_sdk_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection that causes the cycle in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CyclicConnectionFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> CyclicConnectionFlowValidationDetails:
    out: CyclicConnectionFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    else:
        raise DeserializationError(
            "CyclicConnectionFlowValidationDetails.connection required"
        )
    return out
