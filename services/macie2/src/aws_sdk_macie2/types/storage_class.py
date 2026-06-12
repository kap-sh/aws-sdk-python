"""Generated from Smithy shape ``com.amazonaws.macie2#StorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>The storage class of the S3 object. Possible values are:</p>"""
StorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "STANDARD_IA",
    "INTELLIGENT_TIERING",
    "DEEP_ARCHIVE",
    "ONEZONE_IA",
    "GLACIER",
    "GLACIER_IR",
    "OUTPOSTS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "REDUCED_REDUNDANCY",
        "STANDARD_IA",
        "INTELLIGENT_TIERING",
        "DEEP_ARCHIVE",
        "ONEZONE_IA",
        "GLACIER",
        "GLACIER_IR",
        "OUTPOSTS",
    )
)


def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageClass value: {data!r}")
    return cast(StorageClass, data)
