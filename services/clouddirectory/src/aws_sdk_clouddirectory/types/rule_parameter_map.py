"""Generated from Smithy shape ``com.amazonaws.clouddirectory#RuleParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_clouddirectory.types.rule_parameter_key
    import aws_sdk_clouddirectory.types.rule_parameter_value

RuleParameterMap: TypeAlias = dict[
    "aws_sdk_clouddirectory.types.rule_parameter_key.RuleParameterKey",
    "aws_sdk_clouddirectory.types.rule_parameter_value.RuleParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: RuleParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> RuleParameterMap:
    out: RuleParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
