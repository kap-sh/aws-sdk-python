"""Generated from Smithy shape ``com.amazonaws.appstream#StorageConnectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

"""<p>The type of storage connector.</p>"""
StorageConnectorType: TypeAlias = Literal[
    "HOMEFOLDERS",
    "GOOGLE_DRIVE",
    "ONE_DRIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOMEFOLDERS",
        "GOOGLE_DRIVE",
        "ONE_DRIVE",
    )
)


def serialize_aws_json_1_1(value: StorageConnectorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageConnectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageConnectorType value: {data!r}")
    return cast(StorageConnectorType, data)
