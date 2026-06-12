"""Generated from Smithy shape ``com.amazonaws.fsx#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fsx.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "FILE_SYSTEM",
    "VOLUME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FILE_SYSTEM",
        "VOLUME",
    )
)


def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
