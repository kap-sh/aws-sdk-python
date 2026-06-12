"""Generated from Smithy shape ``com.amazonaws.imagebuilder#VulnerablePackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.vulnerable_package

VulnerablePackageList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.vulnerable_package.VulnerablePackage"
]


# --- restJson1 ser/de ---
def serialize_json(value: VulnerablePackageList) -> list:
    import aws_sdk_imagebuilder.types.vulnerable_package

    out: list = []
    for item in value:
        out.append(aws_sdk_imagebuilder.types.vulnerable_package.serialize_json(item))
    return out


def deserialize_json(data: list) -> VulnerablePackageList:
    import aws_sdk_imagebuilder.types.vulnerable_package

    out: VulnerablePackageList = []
    for item in data:
        out.append(aws_sdk_imagebuilder.types.vulnerable_package.deserialize_json(item))
    return out
