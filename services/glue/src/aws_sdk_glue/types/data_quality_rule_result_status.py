"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DataQualityRuleResultStatus: TypeAlias = Literal[
    "PASS",
    "FAIL",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASS",
        "FAIL",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: DataQualityRuleResultStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataQualityRuleResultStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DataQualityRuleResultStatus value: {data!r}"
        )
    return cast(DataQualityRuleResultStatus, data)
