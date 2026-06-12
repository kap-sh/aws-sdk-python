"""Generated from Smithy shape ``com.amazonaws.codeartifact#SuccessfulPackageVersionInfoMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeartifact.types.package_version
    import aws_sdk_codeartifact.types.successful_package_version_info

SuccessfulPackageVersionInfoMap: TypeAlias = dict[
    "aws_sdk_codeartifact.types.package_version.PackageVersion",
    "aws_sdk_codeartifact.types.successful_package_version_info.SuccessfulPackageVersionInfo",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SuccessfulPackageVersionInfoMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_codeartifact.types.successful_package_version_info

        out[key] = (
            aws_sdk_codeartifact.types.successful_package_version_info.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> SuccessfulPackageVersionInfoMap:
    out: SuccessfulPackageVersionInfoMap = {}
    for key, value in data.items():
        import aws_sdk_codeartifact.types.successful_package_version_info

        out[key] = (
            aws_sdk_codeartifact.types.successful_package_version_info.deserialize_json(
                value
            )
        )
    return out
