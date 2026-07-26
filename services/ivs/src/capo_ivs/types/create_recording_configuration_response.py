"""Generated from Smithy shape ``com.amazonaws.ivs#CreateRecordingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.recording_configuration


class CreateRecordingConfigurationResponse(TypedDict, closed=True):
    recording_configuration: NotRequired[
        "capo_ivs.types.recording_configuration.RecordingConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecordingConfigurationResponse) -> dict:
    out: dict = {}
    if "recording_configuration" in value:
        import capo_ivs.types.recording_configuration

        out["recordingConfiguration"] = (
            capo_ivs.types.recording_configuration.serialize_json(
                value["recording_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRecordingConfigurationResponse:
    out: CreateRecordingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "recordingConfiguration" in data:
        import capo_ivs.types.recording_configuration

        out["recording_configuration"] = (
            capo_ivs.types.recording_configuration.deserialize_json(
                data["recordingConfiguration"]
            )
        )
    return out
