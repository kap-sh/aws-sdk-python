"""Generated from Smithy shape ``com.amazonaws.ssm#StepPreviewMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.impact_type
    import aws_sdk_ssm.types.integer

StepPreviewMap: TypeAlias = dict[
    "aws_sdk_ssm.types.impact_type.ImpactType", "aws_sdk_ssm.types.integer.Integer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: StepPreviewMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_ssm.types.impact_type

        out[aws_sdk_ssm.types.impact_type.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> StepPreviewMap:
    out: StepPreviewMap = {}
    for key, value in data.items():
        import aws_sdk_ssm.types.impact_type

        out[aws_sdk_ssm.types.impact_type.deserialize_aws_json_1_1(key)] = value
    return out
