"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_dash_role_caption
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.accessibility_type
    import aws_sdk_medialive.types.caption_destination_settings
    import aws_sdk_medialive.types.dvb_dash_accessibility


class CaptionDescription(TypedDict, closed=True):
    accessibility: NotRequired[
        "aws_sdk_medialive.types.accessibility_type.AccessibilityType"
    ]
    """Indicates whether the caption track implements accessibility features such as written descriptions of spoken dialog, music, and sounds. This signaling is added to HLS output group and MediaPackage output group."""
    caption_selector_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Specifies which input caption selector to use as a caption source when generating output captions. This field should match a captionSelector name."""
    destination_settings: NotRequired[
        "aws_sdk_medialive.types.caption_destination_settings.CaptionDestinationSettings"
    ]
    """Additional settings for captions destination that depend on the destination type."""
    language_code: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """ISO 639-2 three-digit code: http://www.loc.gov/standards/iso639-2/"""
    language_description: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Human readable information to indicate captions available for players (eg. English, or Spanish)."""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Name of the caption description. Used to associate a caption description with an output. Names must be unique within an event."""
    caption_dash_roles: NotRequired[
        "aws_sdk_medialive.types.__list_of_dash_role_caption.__listOfDashRoleCaption"
    ]
    """Identifies the DASH roles to assign to this captions output. Applies only when the captions output is configured for DVB DASH accessibility signaling."""
    dvb_dash_accessibility: NotRequired[
        "aws_sdk_medialive.types.dvb_dash_accessibility.DvbDashAccessibility"
    ]
    """Identifies DVB DASH accessibility signaling in this captions output. Used in Microsoft Smooth Streaming outputs to signal accessibility information to packagers."""


# --- restJson1 ser/de ---
def serialize_json(value: CaptionDescription) -> dict:
    out: dict = {}
    if "accessibility" in value:
        import aws_sdk_medialive.types.accessibility_type

        out["accessibility"] = (
            aws_sdk_medialive.types.accessibility_type.serialize_json(
                value["accessibility"]
            )
        )
    if "caption_selector_name" in value:
        out["captionSelectorName"] = value["caption_selector_name"]
    if "destination_settings" in value:
        import aws_sdk_medialive.types.caption_destination_settings

        out["destinationSettings"] = (
            aws_sdk_medialive.types.caption_destination_settings.serialize_json(
                value["destination_settings"]
            )
        )
    if "language_code" in value:
        out["languageCode"] = value["language_code"]
    if "language_description" in value:
        out["languageDescription"] = value["language_description"]
    if "name" in value:
        out["name"] = value["name"]
    if "caption_dash_roles" in value:
        import aws_sdk_medialive.types.__list_of_dash_role_caption

        out["captionDashRoles"] = (
            aws_sdk_medialive.types.__list_of_dash_role_caption.serialize_json(
                value["caption_dash_roles"]
            )
        )
    if "dvb_dash_accessibility" in value:
        import aws_sdk_medialive.types.dvb_dash_accessibility

        out["dvbDashAccessibility"] = (
            aws_sdk_medialive.types.dvb_dash_accessibility.serialize_json(
                value["dvb_dash_accessibility"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionDescription:
    out: CaptionDescription = {}  # type: ignore[typeddict-item]
    if "accessibility" in data:
        import aws_sdk_medialive.types.accessibility_type

        out["accessibility"] = (
            aws_sdk_medialive.types.accessibility_type.deserialize_json(
                data["accessibility"]
            )
        )
    if "captionSelectorName" in data:
        out["caption_selector_name"] = data["captionSelectorName"]
    if "destinationSettings" in data:
        import aws_sdk_medialive.types.caption_destination_settings

        out["destination_settings"] = (
            aws_sdk_medialive.types.caption_destination_settings.deserialize_json(
                data["destinationSettings"]
            )
        )
    if "languageCode" in data:
        out["language_code"] = data["languageCode"]
    if "languageDescription" in data:
        out["language_description"] = data["languageDescription"]
    if "name" in data:
        out["name"] = data["name"]
    if "captionDashRoles" in data:
        import aws_sdk_medialive.types.__list_of_dash_role_caption

        out["caption_dash_roles"] = (
            aws_sdk_medialive.types.__list_of_dash_role_caption.deserialize_json(
                data["captionDashRoles"]
            )
        )
    if "dvbDashAccessibility" in data:
        import aws_sdk_medialive.types.dvb_dash_accessibility

        out["dvb_dash_accessibility"] = (
            aws_sdk_medialive.types.dvb_dash_accessibility.deserialize_json(
                data["dvbDashAccessibility"]
            )
        )
    return out
