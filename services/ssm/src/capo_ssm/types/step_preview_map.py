"""Generated from Smithy shape ``com.amazonaws.ssm#StepPreviewMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.impact_type
    import capo_ssm.types.integer

StepPreviewMap: TypeAlias = dict[
    "capo_ssm.types.impact_type.ImpactType", "capo_ssm.types.integer.Integer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: StepPreviewMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_ssm.types.impact_type

        out[capo_ssm.types.impact_type.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> StepPreviewMap:
    out: StepPreviewMap = {}
    for key, value in data.items():
        import capo_ssm.types.impact_type

        if value is None:
            continue
        out[capo_ssm.types.impact_type.deserialize_aws_json_1_1(key)] = value
    return out
