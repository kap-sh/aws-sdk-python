"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableECSServiceFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.exportable_ecs_service_field

ExportableECSServiceFields: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.exportable_ecs_service_field.ExportableECSServiceField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableECSServiceFields) -> list:
    import aws_sdk_compute_optimizer.types.exportable_ecs_service_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_ecs_service_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableECSServiceFields:
    import aws_sdk_compute_optimizer.types.exportable_ecs_service_field

    out: ExportableECSServiceFields = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_ecs_service_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
