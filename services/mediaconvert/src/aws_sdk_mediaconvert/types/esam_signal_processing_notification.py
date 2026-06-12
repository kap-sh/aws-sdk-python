"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EsamSignalProcessingNotification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_pattern_sn_signal_processing_notification_ns


class EsamSignalProcessingNotification(TypedDict):
    scc_xml: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_sn_signal_processing_notification_ns.__stringPatternSNSignalProcessingNotificationNS"
    ]
    """Provide your ESAM SignalProcessingNotification XML document inside your JSON job settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The transcoder will use the signal processing instructions in the message that you supply. For your MPEG2-TS file outputs, if you want the service to place SCTE-35 markers at the insertion points you specify in the XML document, you must also enable SCTE-35 ESAM. Note that you can either specify an ESAM XML document or enable SCTE-35 passthrough. You can't do both."""


# --- restJson1 ser/de ---
def serialize_json(value: EsamSignalProcessingNotification) -> dict:
    out: dict = {}
    if "scc_xml" in value:
        out["sccXml"] = value["scc_xml"]
    return out


def deserialize_json(data: dict) -> EsamSignalProcessingNotification:
    out: EsamSignalProcessingNotification = {}  # type: ignore[typeddict-item]
    if "sccXml" in data:
        out["scc_xml"] = data["sccXml"]
    return out
