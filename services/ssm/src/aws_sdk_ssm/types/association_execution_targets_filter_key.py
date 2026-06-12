"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTargetsFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AssociationExecutionTargetsFilterKey: TypeAlias = Literal[
    "Status",
    "ResourceId",
    "ResourceType",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Status",
        "ResourceId",
        "ResourceType",
    )
)


def serialize_aws_json_1_1(value: AssociationExecutionTargetsFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationExecutionTargetsFilterKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssociationExecutionTargetsFilterKey value: {data!r}"
        )
    return cast(AssociationExecutionTargetsFilterKey, data)
