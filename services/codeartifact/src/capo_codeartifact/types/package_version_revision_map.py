"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageVersionRevisionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeartifact.types.package_version
    import capo_codeartifact.types.package_version_revision

PackageVersionRevisionMap: TypeAlias = dict[
    "capo_codeartifact.types.package_version.PackageVersion",
    "capo_codeartifact.types.package_version_revision.PackageVersionRevision",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PackageVersionRevisionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PackageVersionRevisionMap:
    out: PackageVersionRevisionMap = {}
    for key, value in data.items():
        out[key] = value
    return out
