"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseConversionTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.license_conversion_task

LicenseConversionTasks: TypeAlias = list[
    "aws_sdk_license_manager.types.license_conversion_task.LicenseConversionTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseConversionTasks) -> list:
    import aws_sdk_license_manager.types.license_conversion_task

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.license_conversion_task.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseConversionTasks:
    import aws_sdk_license_manager.types.license_conversion_task

    out: LicenseConversionTasks = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.license_conversion_task.deserialize_aws_json_1_1(
                item
            )
        )
    return out
