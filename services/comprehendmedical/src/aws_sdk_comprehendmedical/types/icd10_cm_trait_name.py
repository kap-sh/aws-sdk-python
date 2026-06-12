"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMTraitName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

ICD10CMTraitName: TypeAlias = Literal[
    "NEGATION",
    "DIAGNOSIS",
    "SIGN",
    "SYMPTOM",
    "PERTAINS_TO_FAMILY",
    "HYPOTHETICAL",
    "LOW_CONFIDENCE",
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
    )
)


def serialize_aws_json_1_1(value: ICD10CMTraitName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMTraitName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ICD10CMTraitName value: {data!r}")
    return cast(ICD10CMTraitName, data)
