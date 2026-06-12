"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationStatusName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AssociationStatusName: TypeAlias = Literal[
    "Pending",
    "Success",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Pending",
        "Success",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: AssociationStatusName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationStatusName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationStatusName value: {data!r}")
    return cast(AssociationStatusName, data)
