"""Generated from Smithy shape ``com.amazonaws.odb#ExternalIdType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

ExternalIdType: TypeAlias = Literal[
    "database_ocid",
    "compartment_ocid",
    "tenant_ocid",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "database_ocid",
        "compartment_ocid",
        "tenant_ocid",
    )
)


def serialize_aws_json_1_0(value: ExternalIdType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExternalIdType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExternalIdType value: {data!r}")
    return cast(ExternalIdType, data)
