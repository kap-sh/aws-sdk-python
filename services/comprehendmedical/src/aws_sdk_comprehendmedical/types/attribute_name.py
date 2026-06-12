"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#AttributeName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

AttributeName: TypeAlias = Literal[
    "SIGN",
    "SYMPTOM",
    "DIAGNOSIS",
    "NEGATION",
    "PERTAINS_TO_FAMILY",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "PAST_HISTORY",
    "FUTURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIGN",
        "SYMPTOM",
        "DIAGNOSIS",
        "NEGATION",
        "PERTAINS_TO_FAMILY",
        "HYPOTHETICAL",
        "LOW_CONFIDENCE",
        "PAST_HISTORY",
        "FUTURE",
    )
)


def serialize_aws_json_1_1(value: AttributeName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttributeName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AttributeName value: {data!r}")
    return cast(AttributeName, data)
