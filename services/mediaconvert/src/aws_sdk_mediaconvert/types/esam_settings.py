"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EsamSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer_min0_max30000
    import aws_sdk_mediaconvert.types.esam_manifest_confirm_condition_notification
    import aws_sdk_mediaconvert.types.esam_signal_processing_notification


class EsamSettings(TypedDict, closed=True):
    manifest_confirm_condition_notification: NotRequired[
        "aws_sdk_mediaconvert.types.esam_manifest_confirm_condition_notification.EsamManifestConfirmConditionNotification"
    ]
    """Specifies an ESAM ManifestConfirmConditionNotification XML as per OC-SP-ESAM-API-I03-131025. The transcoder uses the manifest conditioning instructions that you provide in the setting MCC XML."""
    response_signal_preroll: NotRequired[
        "aws_sdk_mediaconvert.types.__integer_min0_max30000.__integerMin0Max30000"
    ]
    """Specifies the stream distance, in milliseconds, between the SCTE 35 messages that the transcoder places and the splice points that they refer to. If the time between the start of the asset and the SCTE-35 message is less than this value, then the transcoder places the SCTE-35 marker at the beginning of the stream."""
    signal_processing_notification: NotRequired[
        "aws_sdk_mediaconvert.types.esam_signal_processing_notification.EsamSignalProcessingNotification"
    ]
    """Specifies an ESAM SignalProcessingNotification XML as per OC-SP-ESAM-API-I03-131025. The transcoder uses the signal processing instructions that you provide in the setting SCC XML."""


# --- restJson1 ser/de ---
def serialize_json(value: EsamSettings) -> dict:
    out: dict = {}
    if "manifest_confirm_condition_notification" in value:
        import aws_sdk_mediaconvert.types.esam_manifest_confirm_condition_notification

        out["manifestConfirmConditionNotification"] = (
            aws_sdk_mediaconvert.types.esam_manifest_confirm_condition_notification.serialize_json(
                value["manifest_confirm_condition_notification"]
            )
        )
    if "response_signal_preroll" in value:
        out["responseSignalPreroll"] = value["response_signal_preroll"]
    if "signal_processing_notification" in value:
        import aws_sdk_mediaconvert.types.esam_signal_processing_notification

        out["signalProcessingNotification"] = (
            aws_sdk_mediaconvert.types.esam_signal_processing_notification.serialize_json(
                value["signal_processing_notification"]
            )
        )
    return out


def deserialize_json(data: dict) -> EsamSettings:
    out: EsamSettings = {}  # type: ignore[typeddict-item]
    if "manifestConfirmConditionNotification" in data:
        import aws_sdk_mediaconvert.types.esam_manifest_confirm_condition_notification

        out["manifest_confirm_condition_notification"] = (
            aws_sdk_mediaconvert.types.esam_manifest_confirm_condition_notification.deserialize_json(
                data["manifestConfirmConditionNotification"]
            )
        )
    if "responseSignalPreroll" in data:
        out["response_signal_preroll"] = data["responseSignalPreroll"]
    if "signalProcessingNotification" in data:
        import aws_sdk_mediaconvert.types.esam_signal_processing_notification

        out["signal_processing_notification"] = (
            aws_sdk_mediaconvert.types.esam_signal_processing_notification.deserialize_json(
                data["signalProcessingNotification"]
            )
        )
    return out
