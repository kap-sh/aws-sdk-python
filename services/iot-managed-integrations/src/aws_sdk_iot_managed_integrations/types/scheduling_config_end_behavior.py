"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#SchedulingConfigEndBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

SchedulingConfigEndBehavior: TypeAlias = Literal[
    "STOP_ROLLOUT",
    "CANCEL",
    "FORCE_CANCEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STOP_ROLLOUT",
        "CANCEL",
        "FORCE_CANCEL",
    )
)


def serialize_json(value: SchedulingConfigEndBehavior) -> str:
    return value


def deserialize_json(data: str) -> SchedulingConfigEndBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SchedulingConfigEndBehavior value: {data!r}"
        )
    return cast(SchedulingConfigEndBehavior, data)
