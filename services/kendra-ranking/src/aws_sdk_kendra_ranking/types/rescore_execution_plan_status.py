"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreExecutionPlanStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra_ranking.errors import DeserializationError

RescoreExecutionPlanStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_aws_json_1_0(value: RescoreExecutionPlanStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RescoreExecutionPlanStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RescoreExecutionPlanStatus value: {data!r}"
        )
    return cast(RescoreExecutionPlanStatus, data)
