"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

MaintenanceWindowTaskType: TypeAlias = Literal[
    "RUN_COMMAND",
    "AUTOMATION",
    "STEP_FUNCTIONS",
    "LAMBDA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUN_COMMAND",
        "AUTOMATION",
        "STEP_FUNCTIONS",
        "LAMBDA",
    )
)


def serialize_aws_json_1_1(value: MaintenanceWindowTaskType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowTaskType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaintenanceWindowTaskType value: {data!r}")
    return cast(MaintenanceWindowTaskType, data)
