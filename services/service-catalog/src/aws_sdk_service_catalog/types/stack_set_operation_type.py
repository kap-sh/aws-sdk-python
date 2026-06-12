"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackSetOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

StackSetOperationType: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE",
        "UPDATE",
        "DELETE",
    )
)


def serialize_aws_json_1_1(value: StackSetOperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StackSetOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StackSetOperationType value: {data!r}")
    return cast(StackSetOperationType, data)
