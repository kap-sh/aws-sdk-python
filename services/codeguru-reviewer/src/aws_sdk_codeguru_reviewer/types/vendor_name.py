"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#VendorName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

VendorName: TypeAlias = Literal[
    "GitHub",
    "GitLab",
    "NativeS3",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GitHub",
        "GitLab",
        "NativeS3",
    )
)


def serialize_json(value: VendorName) -> str:
    return value


def deserialize_json(data: str) -> VendorName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VendorName value: {data!r}")
    return cast(VendorName, data)
