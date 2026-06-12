"""Generated from Smithy shape ``com.amazonaws.sagemaker#ObjectiveStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ObjectiveStatus: TypeAlias = Literal[
    "Succeeded",
    "Pending",
    "Failed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Succeeded",
        "Pending",
        "Failed",
    )
)


def serialize_aws_json_1_1(value: ObjectiveStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectiveStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectiveStatus value: {data!r}")
    return cast(ObjectiveStatus, data)
