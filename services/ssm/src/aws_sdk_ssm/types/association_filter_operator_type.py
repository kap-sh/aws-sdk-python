"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationFilterOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AssociationFilterOperatorType: TypeAlias = Literal[
    "EQUAL",
    "LESS_THAN",
    "GREATER_THAN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUAL",
        "LESS_THAN",
        "GREATER_THAN",
    )
)


def serialize_aws_json_1_1(value: AssociationFilterOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssociationFilterOperatorType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssociationFilterOperatorType value: {data!r}"
        )
    return cast(AssociationFilterOperatorType, data)
