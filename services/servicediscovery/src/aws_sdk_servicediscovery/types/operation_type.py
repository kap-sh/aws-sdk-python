"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

OperationType: TypeAlias = Literal[
    "CREATE_NAMESPACE",
    "DELETE_NAMESPACE",
    "UPDATE_NAMESPACE",
    "UPDATE_SERVICE",
    "REGISTER_INSTANCE",
    "DEREGISTER_INSTANCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_NAMESPACE",
        "DELETE_NAMESPACE",
        "UPDATE_NAMESPACE",
        "UPDATE_SERVICE",
        "REGISTER_INSTANCE",
        "DEREGISTER_INSTANCE",
    )
)


def serialize_aws_json_1_1(value: OperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationType value: {data!r}")
    return cast(OperationType, data)
