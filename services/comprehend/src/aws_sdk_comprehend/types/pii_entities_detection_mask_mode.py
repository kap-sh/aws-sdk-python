"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntitiesDetectionMaskMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

PiiEntitiesDetectionMaskMode: TypeAlias = Literal[
    "MASK",
    "REPLACE_WITH_PII_ENTITY_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MASK",
        "REPLACE_WITH_PII_ENTITY_TYPE",
    )
)


def serialize_aws_json_1_1(value: PiiEntitiesDetectionMaskMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PiiEntitiesDetectionMaskMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PiiEntitiesDetectionMaskMode value: {data!r}"
        )
    return cast(PiiEntitiesDetectionMaskMode, data)
