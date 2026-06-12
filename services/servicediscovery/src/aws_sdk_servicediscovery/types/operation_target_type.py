"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

OperationTargetType: TypeAlias = Literal[
    "NAMESPACE",
    "SERVICE",
    "INSTANCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAMESPACE",
        "SERVICE",
        "INSTANCE",
    )
)


def serialize_aws_json_1_1(value: OperationTargetType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationTargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationTargetType value: {data!r}")
    return cast(OperationTargetType, data)
