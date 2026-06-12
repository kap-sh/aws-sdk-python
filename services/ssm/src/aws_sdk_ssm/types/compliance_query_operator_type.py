"""Generated from Smithy shape ``com.amazonaws.ssm#ComplianceQueryOperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

ComplianceQueryOperatorType: TypeAlias = Literal[
    "EQUAL",
    "NOT_EQUAL",
    "BEGIN_WITH",
    "LESS_THAN",
    "GREATER_THAN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUAL",
        "NOT_EQUAL",
        "BEGIN_WITH",
        "LESS_THAN",
        "GREATER_THAN",
    )
)


def serialize_aws_json_1_1(value: ComplianceQueryOperatorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComplianceQueryOperatorType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ComplianceQueryOperatorType value: {data!r}"
        )
    return cast(ComplianceQueryOperatorType, data)
