"""Generated from Smithy shape ``com.amazonaws.medialive#FeatureActivationsInputPrepareScheduleActions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Feature Activations Input Prepare Schedule Actions"""
FeatureActivationsInputPrepareScheduleActions: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: FeatureActivationsInputPrepareScheduleActions) -> str:
    return value


def deserialize_json(data: str) -> FeatureActivationsInputPrepareScheduleActions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FeatureActivationsInputPrepareScheduleActions value: {data!r}"
        )
    return cast(FeatureActivationsInputPrepareScheduleActions, data)
