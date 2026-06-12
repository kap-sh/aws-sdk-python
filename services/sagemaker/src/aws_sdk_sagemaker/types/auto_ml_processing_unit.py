"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLProcessingUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLProcessingUnit: TypeAlias = Literal[
    "CPU",
    "GPU",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CPU",
        "GPU",
    )
)


def serialize_aws_json_1_1(value: AutoMLProcessingUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLProcessingUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLProcessingUnit value: {data!r}")
    return cast(AutoMLProcessingUnit, data)
