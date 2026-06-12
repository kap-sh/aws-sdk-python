"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableIdleFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.exportable_idle_field

ExportableIdleFields: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.exportable_idle_field.ExportableIdleField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableIdleFields) -> list:
    import aws_sdk_compute_optimizer.types.exportable_idle_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_idle_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableIdleFields:
    import aws_sdk_compute_optimizer.types.exportable_idle_field

    out: ExportableIdleFields = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_idle_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
