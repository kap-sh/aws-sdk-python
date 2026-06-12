"""Generated from Smithy shape ``com.amazonaws.servicecatalog#Replacement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

Replacement: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "CONDITIONAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUE",
        "FALSE",
        "CONDITIONAL",
    )
)


def serialize_aws_json_1_1(value: Replacement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Replacement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Replacement value: {data!r}")
    return cast(Replacement, data)
