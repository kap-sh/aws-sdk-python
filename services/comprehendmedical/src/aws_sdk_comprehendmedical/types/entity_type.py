"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "MEDICATION",
    "MEDICAL_CONDITION",
    "PROTECTED_HEALTH_INFORMATION",
    "TEST_TREATMENT_PROCEDURE",
    "ANATOMY",
    "TIME_EXPRESSION",
    "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MEDICATION",
        "MEDICAL_CONDITION",
        "PROTECTED_HEALTH_INFORMATION",
        "TEST_TREATMENT_PROCEDURE",
        "ANATOMY",
        "TIME_EXPRESSION",
        "BEHAVIORAL_ENVIRONMENTAL_SOCIAL",
    )
)


def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
