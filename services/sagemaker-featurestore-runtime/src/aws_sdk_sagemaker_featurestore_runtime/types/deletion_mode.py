"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#DeletionMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_featurestore_runtime.errors import DeserializationError

DeletionMode: TypeAlias = Literal[
    "SoftDelete",
    "HardDelete",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SoftDelete",
        "HardDelete",
    )
)


def serialize_json(value: DeletionMode) -> str:
    return value


def deserialize_json(data: str) -> DeletionMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeletionMode value: {data!r}")
    return cast(DeletionMode, data)
