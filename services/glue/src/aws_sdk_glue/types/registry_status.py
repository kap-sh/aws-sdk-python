"""Generated from Smithy shape ``com.amazonaws.glue#RegistryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

RegistryStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: RegistryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegistryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistryStatus value: {data!r}")
    return cast(RegistryStatus, data)
