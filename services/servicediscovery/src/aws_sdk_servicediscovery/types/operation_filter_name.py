"""Generated from Smithy shape ``com.amazonaws.servicediscovery#OperationFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

OperationFilterName: TypeAlias = Literal[
    "NAMESPACE_ID",
    "SERVICE_ID",
    "STATUS",
    "TYPE",
    "UPDATE_DATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAMESPACE_ID",
        "SERVICE_ID",
        "STATUS",
        "TYPE",
        "UPDATE_DATE",
    )
)


def serialize_aws_json_1_1(value: OperationFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationFilterName value: {data!r}")
    return cast(OperationFilterName, data)
