"""Generated from Smithy shape ``com.amazonaws.medialive#Mpeg2FilterSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.temporal_filter_settings


class Mpeg2FilterSettings(TypedDict):
    temporal_filter_settings: NotRequired[
        "aws_sdk_medialive.types.temporal_filter_settings.TemporalFilterSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2FilterSettings) -> dict:
    out: dict = {}
    if "temporal_filter_settings" in value:
        import aws_sdk_medialive.types.temporal_filter_settings

        out["temporalFilterSettings"] = (
            aws_sdk_medialive.types.temporal_filter_settings.serialize_json(
                value["temporal_filter_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Mpeg2FilterSettings:
    out: Mpeg2FilterSettings = {}  # type: ignore[typeddict-item]
    if "temporalFilterSettings" in data:
        import aws_sdk_medialive.types.temporal_filter_settings

        out["temporal_filter_settings"] = (
            aws_sdk_medialive.types.temporal_filter_settings.deserialize_json(
                data["temporalFilterSettings"]
            )
        )
    return out
