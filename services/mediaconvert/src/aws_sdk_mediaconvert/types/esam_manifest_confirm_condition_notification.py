"""Generated from Smithy shape ``com.amazonaws.mediaconvert#EsamManifestConfirmConditionNotification``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_pattern_sn_manifest_confirm_condition_notification_ns


class EsamManifestConfirmConditionNotification(TypedDict):
    mcc_xml: NotRequired[
        "aws_sdk_mediaconvert.types.__string_pattern_sn_manifest_confirm_condition_notification_ns.__stringPatternSNManifestConfirmConditionNotificationNS"
    ]
    """Provide your ESAM ManifestConfirmConditionNotification XML document inside your JSON job settings. Form the XML document as per OC-SP-ESAM-API-I03-131025. The transcoder will use the Manifest Conditioning instructions in the message that you supply."""


# --- restJson1 ser/de ---
def serialize_json(value: EsamManifestConfirmConditionNotification) -> dict:
    out: dict = {}
    if "mcc_xml" in value:
        out["mccXml"] = value["mcc_xml"]
    return out


def deserialize_json(data: dict) -> EsamManifestConfirmConditionNotification:
    out: EsamManifestConfirmConditionNotification = {}  # type: ignore[typeddict-item]
    if "mccXml" in data:
        out["mcc_xml"] = data["mccXml"]
    return out
