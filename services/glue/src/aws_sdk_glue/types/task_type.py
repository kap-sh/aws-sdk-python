"""Generated from Smithy shape ``com.amazonaws.glue#TaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

TaskType: TypeAlias = Literal[
    "EVALUATION",
    "LABELING_SET_GENERATION",
    "IMPORT_LABELS",
    "EXPORT_LABELS",
    "FIND_MATCHES",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EVALUATION",
        "LABELING_SET_GENERATION",
        "IMPORT_LABELS",
        "EXPORT_LABELS",
        "FIND_MATCHES",
    )
)


def serialize_aws_json_1_1(value: TaskType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskType value: {data!r}")
    return cast(TaskType, data)
