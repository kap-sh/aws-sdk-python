"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

ICD10CMAttributeType: TypeAlias = Literal[
    "ACUITY",
    "DIRECTION",
    "SYSTEM_ORGAN_SITE",
    "QUALITY",
    "QUANTITY",
    "TIME_TO_DX_NAME",
    "TIME_EXPRESSION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACUITY",
        "DIRECTION",
        "SYSTEM_ORGAN_SITE",
        "QUALITY",
        "QUANTITY",
        "TIME_TO_DX_NAME",
        "TIME_EXPRESSION",
    )
)


def serialize_aws_json_1_1(value: ICD10CMAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ICD10CMAttributeType value: {data!r}")
    return cast(ICD10CMAttributeType, data)
