"""Generated from Smithy shape ``com.amazonaws.sagemaker#FlowDefinitionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

FlowDefinitionStatus: TypeAlias = Literal[
    "Initializing",
    "Active",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Initializing",
        "Active",
        "Failed",
        "Deleting",
    )
)


def serialize_aws_json_1_1(value: FlowDefinitionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlowDefinitionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowDefinitionStatus value: {data!r}")
    return cast(FlowDefinitionStatus, data)
