"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackInstanceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

StackInstanceStatus: TypeAlias = Literal[
    "CURRENT",
    "OUTDATED",
    "INOPERABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CURRENT",
        "OUTDATED",
        "INOPERABLE",
    )
)


def serialize_aws_json_1_1(value: StackInstanceStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StackInstanceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StackInstanceStatus value: {data!r}")
    return cast(StackInstanceStatus, data)
