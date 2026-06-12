"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTTraitName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

SNOMEDCTTraitName: TypeAlias = Literal[
    "NEGATION",
    "DIAGNOSIS",
    "SIGN",
    "SYMPTOM",
    "PERTAINS_TO_FAMILY",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
    "PAST_HISTORY",
    "FUTURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NEGATION",
        "DIAGNOSIS",
        "SIGN",
        "SYMPTOM",
        "PERTAINS_TO_FAMILY",
        "HYPOTHETICAL",
        "LOW_CONFIDENCE",
        "PAST_HISTORY",
        "FUTURE",
    )
)


def serialize_aws_json_1_1(value: SNOMEDCTTraitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTTraitName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SNOMEDCTTraitName value: {data!r}")
    return cast(SNOMEDCTTraitName, data)
