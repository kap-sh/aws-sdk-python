"""Generated from Smithy shape ``com.amazonaws.ecr#VulnerablePackagesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.vulnerable_package

VulnerablePackagesList: TypeAlias = list[
    "capo_ecr.types.vulnerable_package.VulnerablePackage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VulnerablePackagesList) -> list:
    import capo_ecr.types.vulnerable_package

    out: list = []
    for item in value:
        out.append(capo_ecr.types.vulnerable_package.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VulnerablePackagesList:
    import capo_ecr.types.vulnerable_package

    out: VulnerablePackagesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecr.types.vulnerable_package.deserialize_aws_json_1_1(item))
    return out
