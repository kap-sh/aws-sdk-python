"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseEdition``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DatabaseEdition: TypeAlias = Literal[
    "STANDARD_EDITION",
    "ENTERPRISE_EDITION",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD_EDITION",
        "ENTERPRISE_EDITION",
    )
)


def serialize_aws_json_1_0(value: DatabaseEdition) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DatabaseEdition:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseEdition value: {data!r}")
    return cast(DatabaseEdition, data)
