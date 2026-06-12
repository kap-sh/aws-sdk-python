"""Generated from Smithy shape ``com.amazonaws.ecr#VulnerablePackagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.vulnerable_package

VulnerablePackagesList: TypeAlias = list[
    "aws_sdk_ecr.types.vulnerable_package.VulnerablePackage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VulnerablePackagesList) -> list:
    import aws_sdk_ecr.types.vulnerable_package

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.vulnerable_package.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VulnerablePackagesList:
    import aws_sdk_ecr.types.vulnerable_package

    out: VulnerablePackagesList = []
    for item in data:
        out.append(aws_sdk_ecr.types.vulnerable_package.deserialize_aws_json_1_1(item))
    return out
