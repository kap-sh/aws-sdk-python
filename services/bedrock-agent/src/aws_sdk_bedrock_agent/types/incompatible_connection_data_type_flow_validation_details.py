"""Generated from Smithy shape ``com.amazonaws.bedrockagent#IncompatibleConnectionDataTypeFlowValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_connection_name


class IncompatibleConnectionDataTypeFlowValidationDetails(TypedDict):
    connection: "aws_sdk_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection with incompatible data types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncompatibleConnectionDataTypeFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> IncompatibleConnectionDataTypeFlowValidationDetails:
    out: IncompatibleConnectionDataTypeFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    else:
        raise DeserializationError(
            "IncompatibleConnectionDataTypeFlowValidationDetails.connection required"
        )
    return out
