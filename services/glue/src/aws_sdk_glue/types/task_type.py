"""Generated from Smithy shape ``com.amazonaws.glue#TaskType``."""

from typing import Literal, TypeAlias, cast

TaskType: TypeAlias = Literal[
    "EVALUATION",
    "LABELING_SET_GENERATION",
    "IMPORT_LABELS",
    "EXPORT_LABELS",
    "FIND_MATCHES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TaskType:
    return cast(TaskType, data)
