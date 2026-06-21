"""Generated from Smithy shape ``com.amazonaws.medialive#FeatureActivationsOutputStaticImageOverlayScheduleActions``."""

from typing import Literal, TypeAlias, cast

"""Feature Activations Output Static Image Overlay Schedule Actions"""
FeatureActivationsOutputStaticImageOverlayScheduleActions: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(
    value: FeatureActivationsOutputStaticImageOverlayScheduleActions,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> FeatureActivationsOutputStaticImageOverlayScheduleActions:
    return cast(FeatureActivationsOutputStaticImageOverlayScheduleActions, data)
