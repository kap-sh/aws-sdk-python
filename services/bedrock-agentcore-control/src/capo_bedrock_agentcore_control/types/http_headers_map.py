"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HttpHeadersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.http_header_key
    import capo_bedrock_agentcore_control.types.http_header_value

HttpHeadersMap: TypeAlias = dict[
    "capo_bedrock_agentcore_control.types.http_header_key.HttpHeaderKey",
    "capo_bedrock_agentcore_control.types.http_header_value.HttpHeaderValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: HttpHeadersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> HttpHeadersMap:
    out: HttpHeadersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
