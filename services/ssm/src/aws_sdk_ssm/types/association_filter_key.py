"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AssociationFilterKey: TypeAlias = Literal[
    "InstanceId",
    "Name",
    "AssociationId",
    "AssociationStatusName",
    "LastExecutedBefore",
    "LastExecutedAfter",
    "AssociationName",
    "ResourceGroupName",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "InstanceId",
        "Name",
        "AssociationId",
        "AssociationStatusName",
        "LastExecutedBefore",
        "LastExecutedAfter",
        "AssociationName",
        "ResourceGroupName",
    )
)


def serialize_aws_json_1_1(value: AssociationFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationFilterKey value: {data!r}")
    return cast(AssociationFilterKey, data)
