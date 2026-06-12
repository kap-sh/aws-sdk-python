"""Generated from Smithy shape ``com.amazonaws.directoryservice#DirectoryEdition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

DirectoryEdition: TypeAlias = Literal[
    "Enterprise",
    "Standard",
    "Hybrid",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enterprise",
        "Standard",
        "Hybrid",
    )
)


def serialize_aws_json_1_1(value: DirectoryEdition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DirectoryEdition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DirectoryEdition value: {data!r}")
    return cast(DirectoryEdition, data)
