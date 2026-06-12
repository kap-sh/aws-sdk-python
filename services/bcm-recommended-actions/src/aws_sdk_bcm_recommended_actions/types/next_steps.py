"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#NextSteps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_recommended_actions.types.next_step

NextSteps: TypeAlias = list["aws_sdk_bcm_recommended_actions.types.next_step.NextStep"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NextSteps) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> NextSteps:
    return list(data)
