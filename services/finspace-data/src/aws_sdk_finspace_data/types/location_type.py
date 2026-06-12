"""Generated from Smithy shape ``com.amazonaws.finspacedata#locationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

locationType: TypeAlias = Literal[
    "INGESTION",
    "SAGEMAKER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INGESTION",
        "SAGEMAKER",
    )
)


def serialize_json(value: locationType) -> str:
    return value


def deserialize_json(data: str) -> locationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown locationType value: {data!r}")
    return cast(locationType, data)
