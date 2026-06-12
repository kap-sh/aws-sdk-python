"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTEntityCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

SNOMEDCTEntityCategory: TypeAlias = Literal[
    "MEDICAL_CONDITION",
    "ANATOMY",
    "TEST_TREATMENT_PROCEDURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MEDICAL_CONDITION",
        "ANATOMY",
        "TEST_TREATMENT_PROCEDURE",
    )
)


def serialize_aws_json_1_1(value: SNOMEDCTEntityCategory) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTEntityCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SNOMEDCTEntityCategory value: {data!r}")
    return cast(SNOMEDCTEntityCategory, data)
