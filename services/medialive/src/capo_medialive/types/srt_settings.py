"""Generated from Smithy shape ``com.amazonaws.medialive#SrtSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_srt_caller_source
    import capo_medialive.types.srt_listener_settings


class SrtSettings(TypedDict, closed=True):
    srt_caller_sources: NotRequired[
        "capo_medialive.types.__list_of_srt_caller_source.__listOfSrtCallerSource"
    ]
    srt_listener_settings: NotRequired[
        "capo_medialive.types.srt_listener_settings.SrtListenerSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SrtSettings) -> dict:
    out: dict = {}
    if "srt_caller_sources" in value:
        import capo_medialive.types.__list_of_srt_caller_source

        out["srtCallerSources"] = (
            capo_medialive.types.__list_of_srt_caller_source.serialize_json(
                value["srt_caller_sources"]
            )
        )
    if "srt_listener_settings" in value:
        import capo_medialive.types.srt_listener_settings

        out["srtListenerSettings"] = (
            capo_medialive.types.srt_listener_settings.serialize_json(
                value["srt_listener_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtSettings:
    out: SrtSettings = {}  # type: ignore[typeddict-item]
    if "srtCallerSources" in data:
        import capo_medialive.types.__list_of_srt_caller_source

        out["srt_caller_sources"] = (
            capo_medialive.types.__list_of_srt_caller_source.deserialize_json(
                data["srtCallerSources"]
            )
        )
    if "srtListenerSettings" in data:
        import capo_medialive.types.srt_listener_settings

        out["srt_listener_settings"] = (
            capo_medialive.types.srt_listener_settings.deserialize_json(
                data["srtListenerSettings"]
            )
        )
    return out
