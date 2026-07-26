"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedCustomDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_descriptor


class UpdatedCustomDescriptor(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.custom_descriptor.CustomDescriptor"
    ]
    """<p>The updated custom descriptor value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedCustomDescriptor) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.custom_descriptor

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.custom_descriptor.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedCustomDescriptor:
    out: UpdatedCustomDescriptor = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import capo_bedrock_agentcore_control.types.custom_descriptor

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.custom_descriptor.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
