"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#IgnoredReferenceInputFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ignored_reference_input_field

IgnoredReferenceInputFields: TypeAlias = list[
    "capo_bedrock_agentcore.types.ignored_reference_input_field.IgnoredReferenceInputField"
]


# --- restJson1 ser/de ---
def serialize_json(value: IgnoredReferenceInputFields) -> list:
    return list(value)


def deserialize_json(data: list) -> IgnoredReferenceInputFields:
    return [item for item in data if item is not None]
