"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ICD10CMRelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

ICD10CMRelationshipType: TypeAlias = Literal[
    "OVERLAP",
    "SYSTEM_ORGAN_SITE",
    "QUALITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OVERLAP",
        "SYSTEM_ORGAN_SITE",
        "QUALITY",
    )
)


def serialize_aws_json_1_1(value: ICD10CMRelationshipType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ICD10CMRelationshipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ICD10CMRelationshipType value: {data!r}")
    return cast(ICD10CMRelationshipType, data)
