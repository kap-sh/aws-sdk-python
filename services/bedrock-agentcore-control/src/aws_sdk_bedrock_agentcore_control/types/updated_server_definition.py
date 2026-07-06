"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedServerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.server_definition


class UpdatedServerDefinition(TypedDict, closed=True):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.server_definition.ServerDefinition"
    ]
    """<p>The updated server definition value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedServerDefinition) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.server_definition

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.server_definition.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedServerDefinition:
    out: UpdatedServerDefinition = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.server_definition

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.server_definition.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
