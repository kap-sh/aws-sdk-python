"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AccessLevelFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

AccessLevelFilterKey: TypeAlias = Literal[
    "Account",
    "Role",
    "User",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Account",
        "Role",
        "User",
    )
)


def serialize_aws_json_1_1(value: AccessLevelFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessLevelFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessLevelFilterKey value: {data!r}")
    return cast(AccessLevelFilterKey, data)
