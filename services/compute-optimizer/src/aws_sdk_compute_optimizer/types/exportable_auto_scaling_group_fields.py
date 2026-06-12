"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableAutoScalingGroupFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.exportable_auto_scaling_group_field

ExportableAutoScalingGroupFields: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.exportable_auto_scaling_group_field.ExportableAutoScalingGroupField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableAutoScalingGroupFields) -> list:
    import aws_sdk_compute_optimizer.types.exportable_auto_scaling_group_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_auto_scaling_group_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableAutoScalingGroupFields:
    import aws_sdk_compute_optimizer.types.exportable_auto_scaling_group_field

    out: ExportableAutoScalingGroupFields = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_auto_scaling_group_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
