"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseOperationFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.license_operation_failure

LicenseOperationFailureList: TypeAlias = list[
    "capo_license_manager.types.license_operation_failure.LicenseOperationFailure"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseOperationFailureList) -> list:
    import capo_license_manager.types.license_operation_failure

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.license_operation_failure.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseOperationFailureList:
    import capo_license_manager.types.license_operation_failure

    out: LicenseOperationFailureList = []
    for item in data:
        out.append(
            capo_license_manager.types.license_operation_failure.deserialize_aws_json_1_1(
                item
            )
        )
    return out
