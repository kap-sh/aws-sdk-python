"""Generated from Smithy shape ``com.amazonaws.bedrockagent#DeleteFlowVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.numerical_version


class DeleteFlowVersionResponse(TypedDict, closed=True):
    id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the flow.</p>"""
    version: "aws_sdk_bedrock_agent.types.numerical_version.NumericalVersion"
    """<p>The version of the flow being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFlowVersionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["version"] = value["version"]
    return out


def deserialize_json(data: dict) -> DeleteFlowVersionResponse:
    out: DeleteFlowVersionResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DeleteFlowVersionResponse.id required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("DeleteFlowVersionResponse.version required")
    return out
