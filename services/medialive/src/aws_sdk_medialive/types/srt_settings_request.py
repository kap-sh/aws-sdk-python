"""Generated from Smithy shape ``com.amazonaws.medialive#SrtSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_srt_caller_source_request
    import aws_sdk_medialive.types.srt_listener_settings_request


class SrtSettingsRequest(TypedDict, closed=True):
    srt_caller_sources: NotRequired[
        "aws_sdk_medialive.types.__list_of_srt_caller_source_request.__listOfSrtCallerSourceRequest"
    ]
    srt_listener_settings: NotRequired[
        "aws_sdk_medialive.types.srt_listener_settings_request.SrtListenerSettingsRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SrtSettingsRequest) -> dict:
    out: dict = {}
    if "srt_caller_sources" in value:
        import aws_sdk_medialive.types.__list_of_srt_caller_source_request

        out["srtCallerSources"] = (
            aws_sdk_medialive.types.__list_of_srt_caller_source_request.serialize_json(
                value["srt_caller_sources"]
            )
        )
    if "srt_listener_settings" in value:
        import aws_sdk_medialive.types.srt_listener_settings_request

        out["srtListenerSettings"] = (
            aws_sdk_medialive.types.srt_listener_settings_request.serialize_json(
                value["srt_listener_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SrtSettingsRequest:
    out: SrtSettingsRequest = {}  # type: ignore[typeddict-item]
    if "srtCallerSources" in data:
        import aws_sdk_medialive.types.__list_of_srt_caller_source_request

        out["srt_caller_sources"] = (
            aws_sdk_medialive.types.__list_of_srt_caller_source_request.deserialize_json(
                data["srtCallerSources"]
            )
        )
    if "srtListenerSettings" in data:
        import aws_sdk_medialive.types.srt_listener_settings_request

        out["srt_listener_settings"] = (
            aws_sdk_medialive.types.srt_listener_settings_request.deserialize_json(
                data["srtListenerSettings"]
            )
        )
    return out
