"""Generated from Smithy shape ``com.amazonaws.medialive#FeatureActivationsInputPrepareScheduleActions``."""

from typing import Literal, TypeAlias, cast

"""Feature Activations Input Prepare Schedule Actions"""
FeatureActivationsInputPrepareScheduleActions: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FeatureActivationsInputPrepareScheduleActions) -> str:
    return value


def deserialize_json(data: str) -> FeatureActivationsInputPrepareScheduleActions:
    return cast(FeatureActivationsInputPrepareScheduleActions, data)
