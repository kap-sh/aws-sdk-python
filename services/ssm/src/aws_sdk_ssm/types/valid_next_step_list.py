"""Generated from Smithy shape ``com.amazonaws.ssm#ValidNextStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.valid_next_step

ValidNextStepList: TypeAlias = list["aws_sdk_ssm.types.valid_next_step.ValidNextStep"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ValidNextStepList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ValidNextStepList:
    return list(data)
