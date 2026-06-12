"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableInstanceFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.exportable_instance_field

ExportableInstanceFields: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.exportable_instance_field.ExportableInstanceField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableInstanceFields) -> list:
    import aws_sdk_compute_optimizer.types.exportable_instance_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_instance_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableInstanceFields:
    import aws_sdk_compute_optimizer.types.exportable_instance_field

    out: ExportableInstanceFields = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_instance_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
