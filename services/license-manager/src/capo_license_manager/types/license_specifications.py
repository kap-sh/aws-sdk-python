"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.license_specification

LicenseSpecifications: TypeAlias = list[
    "capo_license_manager.types.license_specification.LicenseSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseSpecifications) -> list:
    import capo_license_manager.types.license_specification

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.license_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LicenseSpecifications:
    import capo_license_manager.types.license_specification

    out: LicenseSpecifications = []
    for item in data:
        out.append(
            capo_license_manager.types.license_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
