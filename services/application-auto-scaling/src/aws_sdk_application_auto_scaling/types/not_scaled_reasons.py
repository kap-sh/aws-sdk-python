"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#NotScaledReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_auto_scaling.types.not_scaled_reason

NotScaledReasons: TypeAlias = list[
    "aws_sdk_application_auto_scaling.types.not_scaled_reason.NotScaledReason"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotScaledReasons) -> list:
    import aws_sdk_application_auto_scaling.types.not_scaled_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_auto_scaling.types.not_scaled_reason.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotScaledReasons:
    import aws_sdk_application_auto_scaling.types.not_scaled_reason

    out: NotScaledReasons = []
    for item in data:
        out.append(
            aws_sdk_application_auto_scaling.types.not_scaled_reason.deserialize_aws_json_1_1(
                item
            )
        )
    return out
