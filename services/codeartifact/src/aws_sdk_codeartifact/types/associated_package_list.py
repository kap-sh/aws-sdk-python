"""Generated from Smithy shape ``com.amazonaws.codeartifact#AssociatedPackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.associated_package

AssociatedPackageList: TypeAlias = list[
    "aws_sdk_codeartifact.types.associated_package.AssociatedPackage"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedPackageList) -> list:
    import aws_sdk_codeartifact.types.associated_package

    out: list = []
    for item in value:
        out.append(aws_sdk_codeartifact.types.associated_package.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedPackageList:
    import aws_sdk_codeartifact.types.associated_package

    out: AssociatedPackageList = []
    for item in data:
        out.append(aws_sdk_codeartifact.types.associated_package.deserialize_json(item))
    return out
