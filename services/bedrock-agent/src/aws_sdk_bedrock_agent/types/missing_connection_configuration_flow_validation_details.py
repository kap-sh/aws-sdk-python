"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MissingConnectionConfigurationFlowValidationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.flow_connection_name


class MissingConnectionConfigurationFlowValidationDetails(TypedDict, closed=True):
    connection: "aws_sdk_bedrock_agent.types.flow_connection_name.FlowConnectionName"
    """<p>The name of the connection missing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MissingConnectionConfigurationFlowValidationDetails) -> dict:
    out: dict = {}
    out["connection"] = value["connection"]
    return out


def deserialize_json(data: dict) -> MissingConnectionConfigurationFlowValidationDetails:
    out: MissingConnectionConfigurationFlowValidationDetails = {}  # type: ignore[typeddict-item]
    if "connection" in data:
        out["connection"] = data["connection"]
    else:
        raise DeserializationError(
            "MissingConnectionConfigurationFlowValidationDetails.connection required"
        )
    return out
