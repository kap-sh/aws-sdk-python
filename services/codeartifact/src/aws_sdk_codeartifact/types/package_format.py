"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageFormat``."""

from typing import Literal, TypeAlias, cast

PackageFormat: TypeAlias = Literal[
    "npm",
    "pypi",
    "maven",
    "nuget",
    "generic",
    "ruby",
    "swift",
    "cargo",
]


# --- restJson1 ser/de ---
def serialize_json(value: PackageFormat) -> str:
    return value


def deserialize_json(data: str) -> PackageFormat:
    return cast(PackageFormat, data)
