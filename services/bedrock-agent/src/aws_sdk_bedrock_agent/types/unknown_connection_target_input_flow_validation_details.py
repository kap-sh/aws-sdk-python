"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UnknownConnectionTargetInputFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_connection_name


class UnknownConnectionTargetInputFlowValidationDetails(TypedDict, closed=True):
    connection: "aws_sdk_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection with the unknown target input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnknownConnectionTargetInputFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> UnknownConnectionTargetInputFlowValidationDetails:
    out: UnknownConnectionTargetInputFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    else:
        raise DeserializationError(
            "UnknownConnectionTargetInputFlowValidationDetails.connection required"
        )
    return out
