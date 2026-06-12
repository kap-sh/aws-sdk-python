"""Generated from Smithy shape ``com.amazonaws.servicecatalog#EngineWorkflowStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

EngineWorkflowStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: EngineWorkflowStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EngineWorkflowStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EngineWorkflowStatus value: {data!r}")
    return cast(EngineWorkflowStatus, data)
