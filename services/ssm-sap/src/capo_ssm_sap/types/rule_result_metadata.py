"""Generated from Smithy shape ``com.amazonaws.ssmsap#RuleResultMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_sap.types.rule_result_metadata_key
    import capo_ssm_sap.types.rule_result_metadata_value

RuleResultMetadata: TypeAlias = dict[
    "capo_ssm_sap.types.rule_result_metadata_key.RuleResultMetadataKey",
    "capo_ssm_sap.types.rule_result_metadata_value.RuleResultMetadataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RuleResultMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RuleResultMetadata:
    out: RuleResultMetadata = {}
    for key, value in data.items():
        out[key] = value
    return out
