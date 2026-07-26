"""Generated from Smithy shape ``com.amazonaws.bedrockagent#AdditionalModelRequestFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.additional_model_request_fields_key
    import capo_bedrock_agent.types.additional_model_request_fields_value

AdditionalModelRequestFields: TypeAlias = dict[
    "capo_bedrock_agent.types.additional_model_request_fields_key.AdditionalModelRequestFieldsKey",
    "capo_bedrock_agent.types.additional_model_request_fields_value.AdditionalModelRequestFieldsValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AdditionalModelRequestFields) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AdditionalModelRequestFields:
    out: AdditionalModelRequestFields = {}
    for key, value in data.items():
        out[key] = value
    return out
