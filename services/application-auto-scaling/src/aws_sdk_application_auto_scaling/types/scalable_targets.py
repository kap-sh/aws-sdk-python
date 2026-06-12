"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalableTargets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.scalable_target

ScalableTargets: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.scalable_target.ScalableTarget"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalableTargets) -> list:
    import aws_sdk_application_auto_scaling.types.scalable_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_auto_scaling.types.scalable_target.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScalableTargets:
    import aws_sdk_application_auto_scaling.types.scalable_target

    out: ScalableTargets = []
    for item in data:
        out.append(
            aws_sdk_application_auto_scaling.types.scalable_target.deserialize_aws_json_1_1(
                item
            )
        )
    return out
