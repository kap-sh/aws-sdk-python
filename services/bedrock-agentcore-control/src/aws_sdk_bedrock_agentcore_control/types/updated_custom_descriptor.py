"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedCustomDescriptor``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.custom_descriptor


class UpdatedCustomDescriptor(TypedDict):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.custom_descriptor.CustomDescriptor"
    ]
    """<p>The updated custom descriptor value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedCustomDescriptor) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.custom_descriptor

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.custom_descriptor.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedCustomDescriptor:
    out: UpdatedCustomDescriptor = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.custom_descriptor

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.custom_descriptor.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
