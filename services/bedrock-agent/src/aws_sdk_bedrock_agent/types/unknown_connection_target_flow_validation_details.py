"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UnknownConnectionTargetFlowValidationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_connection_name


class UnknownConnectionTargetFlowValidationDetails(TypedDict):
    connection: "aws_sdk_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection with the unknown target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnknownConnectionTargetFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> UnknownConnectionTargetFlowValidationDetails:
    out: UnknownConnectionTargetFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    else:
        raise DeserializationError(
            "UnknownConnectionTargetFlowValidationDetails.connection required"
        )
    return out
