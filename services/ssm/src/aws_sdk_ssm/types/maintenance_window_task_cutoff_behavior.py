"""Generated from Smithy shape ``com.amazonaws.ssm#MaintenanceWindowTaskCutoffBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

MaintenanceWindowTaskCutoffBehavior: TypeAlias = Literal[
    "CONTINUE_TASK",
    "CANCEL_TASK",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONTINUE_TASK",
        "CANCEL_TASK",
    )
)


def serialize_aws_json_1_1(value: MaintenanceWindowTaskCutoffBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaintenanceWindowTaskCutoffBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MaintenanceWindowTaskCutoffBehavior value: {data!r}"
        )
    return cast(MaintenanceWindowTaskCutoffBehavior, data)
