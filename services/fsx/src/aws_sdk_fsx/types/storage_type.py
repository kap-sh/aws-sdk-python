"""Generated from Smithy shape ``com.amazonaws.fsx#StorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

"""<p>Specifies the file system's storage type.</p>"""
StorageType: TypeAlias = Literal[
    "SSD",
    "HDD",
    "INTELLIGENT_TIERING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSD",
        "HDD",
        "INTELLIGENT_TIERING",
    )
)


def serialize_aws_json_1_1(value: StorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageType value: {data!r}")
    return cast(StorageType, data)
