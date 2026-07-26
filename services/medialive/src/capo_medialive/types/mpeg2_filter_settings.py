"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2FilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.temporal_filter_settings


class Mpeg2FilterSettings(TypedDict, closed=True):
    temporal_filter_settings: NotRequired[
        "capo_medialive.types.temporal_filter_settings.TemporalFilterSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2FilterSettings) -> dict:
    out: dict = {}
    if "temporal_filter_settings" in value:
        import capo_medialive.types.temporal_filter_settings

        out["temporalFilterSettings"] = (
            capo_medialive.types.temporal_filter_settings.serialize_json(
                value["temporal_filter_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Mpeg2FilterSettings:
    out: Mpeg2FilterSettings = {}  # type: ignore[typeddict-item]
    if "temporalFilterSettings" in data:
        import capo_medialive.types.temporal_filter_settings

        out["temporal_filter_settings"] = (
            capo_medialive.types.temporal_filter_settings.deserialize_json(
                data["temporalFilterSettings"]
            )
        )
    return out
