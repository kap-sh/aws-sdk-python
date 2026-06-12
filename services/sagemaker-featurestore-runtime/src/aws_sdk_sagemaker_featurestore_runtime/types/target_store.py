"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#TargetStore``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_featurestore_runtime.errors import DeserializationError

TargetStore: TypeAlias = Literal[
    "OnlineStore",
    "OfflineStore",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OnlineStore",
        "OfflineStore",
    )
)


def serialize_json(value: TargetStore) -> str:
    return value


def deserialize_json(data: str) -> TargetStore:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetStore value: {data!r}")
    return cast(TargetStore, data)
