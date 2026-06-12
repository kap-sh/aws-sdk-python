"""Generated from Smithy shape ``com.amazonaws.medialive#FeatureActivationsOutputStaticImageOverlayScheduleActions``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Feature Activations Output Static Image Overlay Schedule Actions"""
FeatureActivationsOutputStaticImageOverlayScheduleActions: TypeAlias = Literal[
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


def serialize_json(
    value: FeatureActivationsOutputStaticImageOverlayScheduleActions,
) -> str:
    return value


def deserialize_json(
    data: str,
) -> FeatureActivationsOutputStaticImageOverlayScheduleActions:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown FeatureActivationsOutputStaticImageOverlayScheduleActions value: {data!r}"
        )
    return cast(FeatureActivationsOutputStaticImageOverlayScheduleActions, data)
