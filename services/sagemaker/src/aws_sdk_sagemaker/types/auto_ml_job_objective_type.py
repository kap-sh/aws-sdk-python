"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobObjectiveType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLJobObjectiveType: TypeAlias = Literal[
    "Maximize",
    "Minimize",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Maximize",
        "Minimize",
    )
)


def serialize_aws_json_1_1(value: AutoMLJobObjectiveType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLJobObjectiveType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLJobObjectiveType value: {data!r}")
    return cast(AutoMLJobObjectiveType, data)
