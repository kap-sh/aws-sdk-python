"""Generated from Smithy shape ``com.amazonaws.configservice#ResourceEvaluationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ResourceEvaluationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "FAILED",
        "SUCCEEDED",
    )
)


def serialize_aws_json_1_1(value: ResourceEvaluationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceEvaluationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceEvaluationStatus value: {data!r}")
    return cast(ResourceEvaluationStatus, data)
