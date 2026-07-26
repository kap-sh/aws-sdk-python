"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionErrorMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_error

PackageVersionErrorMap: TypeAlias = dict[
    "capo_codeartifact.types.package_version.PackageVersion",
    "capo_codeartifact.types.package_version_error.PackageVersionError",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PackageVersionErrorMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codeartifact.types.package_version_error

        out[key] = capo_codeartifact.types.package_version_error.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PackageVersionErrorMap:
    out: PackageVersionErrorMap = {}
    for key, value in data.items():
        import capo_codeartifact.types.package_version_error

        out[key] = capo_codeartifact.types.package_version_error.deserialize_json(value)
    return out
