"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ResponseBody``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.content_body

ResponseBody: TypeAlias = dict[
    "str", "capo_bedrock_agent_runtime.types.content_body.ContentBody"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ResponseBody) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_bedrock_agent_runtime.types.content_body

        out[key] = capo_bedrock_agent_runtime.types.content_body.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ResponseBody:
    out: ResponseBody = {}
    for key, value in data.items():
        import capo_bedrock_agent_runtime.types.content_body

        out[key] = capo_bedrock_agent_runtime.types.content_body.deserialize_json(value)
    return out
