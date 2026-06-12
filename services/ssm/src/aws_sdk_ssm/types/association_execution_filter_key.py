"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AssociationExecutionFilterKey: TypeAlias = Literal[
    "ExecutionId",
    "Status",
    "CreatedTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ExecutionId",
        "Status",
        "CreatedTime",
    )
)


def serialize_aws_json_1_1(value: AssociationExecutionFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationExecutionFilterKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssociationExecutionFilterKey value: {data!r}"
        )
    return cast(AssociationExecutionFilterKey, data)
