"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedA2aDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.a2a_descriptor


class UpdatedA2aDescriptor(TypedDict, closed=True):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.a2a_descriptor.A2aDescriptor"
    ]
    """<p>The updated A2A descriptor value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedA2aDescriptor) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.a2a_descriptor

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.a2a_descriptor.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedA2aDescriptor:
    out: UpdatedA2aDescriptor = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.a2a_descriptor

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.a2a_descriptor.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
