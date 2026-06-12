"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ExportableLicenseFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.exportable_license_field

ExportableLicenseFields: TypeAlias = list[
    "aws_sdk_compute_optimizer.types.exportable_license_field.ExportableLicenseField"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportableLicenseFields) -> list:
    import aws_sdk_compute_optimizer.types.exportable_license_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_license_field.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ExportableLicenseFields:
    import aws_sdk_compute_optimizer.types.exportable_license_field

    out: ExportableLicenseFields = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer.types.exportable_license_field.deserialize_aws_json_1_0(
                item
            )
        )
    return out
