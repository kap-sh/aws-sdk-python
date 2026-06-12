"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AccessStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

AccessStatus: TypeAlias = Literal[
    "ENABLED",
    "UNDER_CHANGE",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "UNDER_CHANGE",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: AccessStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccessStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessStatus value: {data!r}")
    return cast(AccessStatus, data)
