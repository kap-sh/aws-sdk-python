"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#SNOMEDCTAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

SNOMEDCTAttributeType: TypeAlias = Literal[
    "ACUITY",
    "QUALITY",
    "DIRECTION",
    "SYSTEM_ORGAN_SITE",
    "TEST_VALUE",
    "TEST_UNIT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACUITY",
        "QUALITY",
        "DIRECTION",
        "SYSTEM_ORGAN_SITE",
        "TEST_VALUE",
        "TEST_UNIT",
    )
)


def serialize_aws_json_1_1(value: SNOMEDCTAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SNOMEDCTAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SNOMEDCTAttributeType value: {data!r}")
    return cast(SNOMEDCTAttributeType, data)
