"""Generated from Smithy shape ``com.amazonaws.codeartifact#PackageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "npm",
        "pypi",
        "maven",
        "nuget",
        "generic",
        "ruby",
        "swift",
        "cargo",
    )
)


def serialize_json(value: PackageFormat) -> str:
    return value


def deserialize_json(data: str) -> PackageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PackageFormat value: {data!r}")
    return cast(PackageFormat, data)
