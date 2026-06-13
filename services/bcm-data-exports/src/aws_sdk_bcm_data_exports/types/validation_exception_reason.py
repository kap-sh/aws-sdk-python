"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "unknownOperation",
    "cannotParse",
    "fieldValidationFailed",
    "other",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "unknownOperation",
        "cannotParse",
        "fieldValidationFailed",
        "other",
    )
)


def serialize_aws_json_1_1(value: ValidationExceptionReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
