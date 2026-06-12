"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageDependencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_dependency

PackageDependencyList: TypeAlias = list[
    "aws_sdk_codeartifact.types.package_dependency.PackageDependency"
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageDependencyList) -> list:
    import aws_sdk_codeartifact.types.package_dependency

    out: list = []
    for item in value:
        out.append(aws_sdk_codeartifact.types.package_dependency.serialize_json(item))
    return out


def deserialize_json(data: list) -> PackageDependencyList:
    import aws_sdk_codeartifact.types.package_dependency

    out: PackageDependencyList = []
    for item in data:
        out.append(aws_sdk_codeartifact.types.package_dependency.deserialize_json(item))
    return out
