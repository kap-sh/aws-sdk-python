"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_optimization_hub.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "FieldValidationFailed",
    "Other",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FieldValidationFailed",
        "Other",
    )
)


def serialize_aws_json_1_0(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
