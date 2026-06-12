"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RequiresRecreation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

RequiresRecreation: TypeAlias = Literal[
    "NEVER",
    "CONDITIONALLY",
    "ALWAYS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEVER",
        "CONDITIONALLY",
        "ALWAYS",
    )
)


def serialize_aws_json_1_1(value: RequiresRecreation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RequiresRecreation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RequiresRecreation value: {data!r}")
    return cast(RequiresRecreation, data)
