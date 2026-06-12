"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableVolumeFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.exportable_volume_field

ExportableVolumeFields: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.exportable_volume_field.ExportableVolumeField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableVolumeFields) -> list:
    import aws_sdk_compute_optimizer.types.exportable_volume_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_volume_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableVolumeFields:
    import aws_sdk_compute_optimizer.types.exportable_volume_field

    out: ExportableVolumeFields = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_volume_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
