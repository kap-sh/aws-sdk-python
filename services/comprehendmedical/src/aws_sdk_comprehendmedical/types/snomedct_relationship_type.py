"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTRelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

SNOMEDCTRelationshipType: TypeAlias = Literal[
    "ACUITY",
    "QUALITY",
    "TEST_VALUE",
    "TEST_UNITS",
    "DIRECTION",
    "SYSTEM_ORGAN_SITE",
    "TEST_UNIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACUITY",
        "QUALITY",
        "TEST_VALUE",
        "TEST_UNITS",
        "DIRECTION",
        "SYSTEM_ORGAN_SITE",
        "TEST_UNIT",
    )
)


def serialize_aws_json_1_1(value: SNOMEDCTRelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTRelationshipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SNOMEDCTRelationshipType value: {data!r}")
    return cast(SNOMEDCTRelationshipType, data)
