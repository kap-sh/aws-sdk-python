"""Generated from Smithy shape ``com.amazonaws.medialive#SrtSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_srt_caller_source
    import aws_sdk_medialive.types.srt_listener_settings


class SrtSettings(TypedDict, closed=True):
    srt_caller_sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_srt_caller_source.__listOfSrtCallerSource"
    ]
    srt_listener_settings: NotRequired[
        "aws_sdk_medialive.types.srt_listener_settings.SrtListenerSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SrtSettings) -> dict:
    out: dict = {}
    if "srt_caller_sources" in value:
        import aws_sdk_medialive.types.__list_of_srt_caller_source

        out["srtCallerSources"] = (
            aws_sdk_medialive.types.__list_of_srt_caller_source.serialize_json(
                value["srt_caller_sources"]
            )
        )
    if "srt_listener_settings" in value:
        import aws_sdk_medialive.types.srt_listener_settings

        out["srtListenerSettings"] = (
            aws_sdk_medialive.types.srt_listener_settings.serialize_json(
                value["srt_listener_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtSettings:
    out: SrtSettings = {}  # type: ignore[typeddict-item]
    if "srtCallerSources" in data:
        import aws_sdk_medialive.types.__list_of_srt_caller_source

        out["srt_caller_sources"] = (
            aws_sdk_medialive.types.__list_of_srt_caller_source.deserialize_json(
                data["srtCallerSources"]
            )
        )
    if "srtListenerSettings" in data:
        import aws_sdk_medialive.types.srt_listener_settings

        out["srt_listener_settings"] = (
            aws_sdk_medialive.types.srt_listener_settings.deserialize_json(
                data["srtListenerSettings"]
            )
        )
    return out
