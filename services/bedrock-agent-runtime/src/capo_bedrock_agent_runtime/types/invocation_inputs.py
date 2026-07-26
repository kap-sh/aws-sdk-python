"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvocationInputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.invocation_input_member

InvocationInputs: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.invocation_input_member.InvocationInputMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvocationInputs) -> list:
    import capo_bedrock_agent_runtime.types.invocation_input_member

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.invocation_input_member.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> InvocationInputs:
    import capo_bedrock_agent_runtime.types.invocation_input_member

    out: InvocationInputs = []
    for item in data:
        out.append(
            capo_bedrock_agent_runtime.types.invocation_input_member.deserialize_json(
                item
            )
        )
    return out
