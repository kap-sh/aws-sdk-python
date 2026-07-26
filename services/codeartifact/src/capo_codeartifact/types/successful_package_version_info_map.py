"""Generated from Smithy shape ``com.amazonaws.codeartifact#SuccessfulPackageVersionInfoMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.successful_package_version_info

SuccessfulPackageVersionInfoMap: TypeAlias = dict[
    "capo_codeartifact.types.package_version.PackageVersion",
    "capo_codeartifact.types.successful_package_version_info.SuccessfulPackageVersionInfo",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SuccessfulPackageVersionInfoMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codeartifact.types.successful_package_version_info

        out[key] = (
            capo_codeartifact.types.successful_package_version_info.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> SuccessfulPackageVersionInfoMap:
    out: SuccessfulPackageVersionInfoMap = {}
    for key, value in data.items():
        import capo_codeartifact.types.successful_package_version_info

        out[key] = (
            capo_codeartifact.types.successful_package_version_info.deserialize_json(
                value
            )
        )
    return out
