"""Generated from Smithy shape ``com.amazonaws.medialive#FailoverConditionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.audio_silence_failover_settings
    import capo_medialive.types.input_loss_failover_settings
    import capo_medialive.types.video_black_failover_settings


class FailoverConditionSettings(TypedDict, closed=True):
    audio_silence_settings: NotRequired[
        "capo_medialive.types.audio_silence_failover_settings.AudioSilenceFailoverSettings"
    ]
    """MediaLive will perform a failover if the specified audio selector is silent for the specified period."""
    input_loss_settings: NotRequired[
        "capo_medialive.types.input_loss_failover_settings.InputLossFailoverSettings"
    ]
    """MediaLive will perform a failover if content is not detected in this input for the specified period."""
    video_black_settings: NotRequired[
        "capo_medialive.types.video_black_failover_settings.VideoBlackFailoverSettings"
    ]
    """MediaLive will perform a failover if content is considered black for the specified period."""


# --- restJson1 ser/de ---
def serialize_json(value: FailoverConditionSettings) -> dict:
    out: dict = {}
    if "audio_silence_settings" in value:
        import capo_medialive.types.audio_silence_failover_settings

        out["audioSilenceSettings"] = (
            capo_medialive.types.audio_silence_failover_settings.serialize_json(
                value["audio_silence_settings"]
            )
        )
    if "input_loss_settings" in value:
        import capo_medialive.types.input_loss_failover_settings

        out["inputLossSettings"] = (
            capo_medialive.types.input_loss_failover_settings.serialize_json(
                value["input_loss_settings"]
            )
        )
    if "video_black_settings" in value:
        import capo_medialive.types.video_black_failover_settings

        out["videoBlackSettings"] = (
            capo_medialive.types.video_black_failover_settings.serialize_json(
                value["video_black_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FailoverConditionSettings:
    out: FailoverConditionSettings = {}  # type: ignore[typeddict-item]
    if "audioSilenceSettings" in data:
        import capo_medialive.types.audio_silence_failover_settings

        out["audio_silence_settings"] = (
            capo_medialive.types.audio_silence_failover_settings.deserialize_json(
                data["audioSilenceSettings"]
            )
        )
    if "inputLossSettings" in data:
        import capo_medialive.types.input_loss_failover_settings

        out["input_loss_settings"] = (
            capo_medialive.types.input_loss_failover_settings.deserialize_json(
                data["inputLossSettings"]
            )
        )
    if "videoBlackSettings" in data:
        import capo_medialive.types.video_black_failover_settings

        out["video_black_settings"] = (
            capo_medialive.types.video_black_failover_settings.deserialize_json(
                data["videoBlackSettings"]
            )
        )
    return out
