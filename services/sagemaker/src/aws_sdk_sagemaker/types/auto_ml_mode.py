"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLMode: TypeAlias = Literal[
    "AUTO",
    "ENSEMBLING",
    "HYPERPARAMETER_TUNING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "ENSEMBLING",
        "HYPERPARAMETER_TUNING",
    )
)


def serialize_aws_json_1_1(value: AutoMLMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLMode value: {data!r}")
    return cast(AutoMLMode, data)
