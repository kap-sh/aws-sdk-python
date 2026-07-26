"""Generated from Smithy shape ``com.amazonaws.b2bi#X12ValidationRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_b2bi.types.x12_validation_rule

X12ValidationRules: TypeAlias = list[
    "capo_b2bi.types.x12_validation_rule.X12ValidationRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: X12ValidationRules) -> list:
    import capo_b2bi.types.x12_validation_rule

    out: list = []
    for item in value:
        out.append(capo_b2bi.types.x12_validation_rule.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> X12ValidationRules:
    import capo_b2bi.types.x12_validation_rule

    out: X12ValidationRules = []
    for item in data:
        out.append(capo_b2bi.types.x12_validation_rule.deserialize_aws_json_1_0(item))
    return out
