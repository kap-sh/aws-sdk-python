"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionSelectorSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.ancillary_source_settings
    import capo_medialive.types.arib_source_settings
    import capo_medialive.types.dvb_sub_source_settings
    import capo_medialive.types.embedded_source_settings
    import capo_medialive.types.scte20_source_settings
    import capo_medialive.types.scte27_source_settings
    import capo_medialive.types.smart_subtitle_source_settings
    import capo_medialive.types.teletext_source_settings


class CaptionSelectorSettings(TypedDict, closed=True):
    ancillary_source_settings: NotRequired[
        "capo_medialive.types.ancillary_source_settings.AncillarySourceSettings"
    ]
    arib_source_settings: NotRequired[
        "capo_medialive.types.arib_source_settings.AribSourceSettings"
    ]
    dvb_sub_source_settings: NotRequired[
        "capo_medialive.types.dvb_sub_source_settings.DvbSubSourceSettings"
    ]
    embedded_source_settings: NotRequired[
        "capo_medialive.types.embedded_source_settings.EmbeddedSourceSettings"
    ]
    scte20_source_settings: NotRequired[
        "capo_medialive.types.scte20_source_settings.Scte20SourceSettings"
    ]
    scte27_source_settings: NotRequired[
        "capo_medialive.types.scte27_source_settings.Scte27SourceSettings"
    ]
    teletext_source_settings: NotRequired[
        "capo_medialive.types.teletext_source_settings.TeletextSourceSettings"
    ]
    smart_subtitle_source_settings: NotRequired[
        "capo_medialive.types.smart_subtitle_source_settings.SmartSubtitleSourceSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionSelectorSettings) -> dict:
    out: dict = {}
    if "ancillary_source_settings" in value:
        import capo_medialive.types.ancillary_source_settings

        out["ancillarySourceSettings"] = (
            capo_medialive.types.ancillary_source_settings.serialize_json(
                value["ancillary_source_settings"]
            )
        )
    if "arib_source_settings" in value:
        import capo_medialive.types.arib_source_settings

        out["aribSourceSettings"] = (
            capo_medialive.types.arib_source_settings.serialize_json(
                value["arib_source_settings"]
            )
        )
    if "dvb_sub_source_settings" in value:
        import capo_medialive.types.dvb_sub_source_settings

        out["dvbSubSourceSettings"] = (
            capo_medialive.types.dvb_sub_source_settings.serialize_json(
                value["dvb_sub_source_settings"]
            )
        )
    if "embedded_source_settings" in value:
        import capo_medialive.types.embedded_source_settings

        out["embeddedSourceSettings"] = (
            capo_medialive.types.embedded_source_settings.serialize_json(
                value["embedded_source_settings"]
            )
        )
    if "scte20_source_settings" in value:
        import capo_medialive.types.scte20_source_settings

        out["scte20SourceSettings"] = (
            capo_medialive.types.scte20_source_settings.serialize_json(
                value["scte20_source_settings"]
            )
        )
    if "scte27_source_settings" in value:
        import capo_medialive.types.scte27_source_settings

        out["scte27SourceSettings"] = (
            capo_medialive.types.scte27_source_settings.serialize_json(
                value["scte27_source_settings"]
            )
        )
    if "teletext_source_settings" in value:
        import capo_medialive.types.teletext_source_settings

        out["teletextSourceSettings"] = (
            capo_medialive.types.teletext_source_settings.serialize_json(
                value["teletext_source_settings"]
            )
        )
    if "smart_subtitle_source_settings" in value:
        import capo_medialive.types.smart_subtitle_source_settings

        out["smartSubtitleSourceSettings"] = (
            capo_medialive.types.smart_subtitle_source_settings.serialize_json(
                value["smart_subtitle_source_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionSelectorSettings:
    out: CaptionSelectorSettings = {}  # type: ignore[typeddict-item]
    if "ancillarySourceSettings" in data:
        import capo_medialive.types.ancillary_source_settings

        out["ancillary_source_settings"] = (
            capo_medialive.types.ancillary_source_settings.deserialize_json(
                data["ancillarySourceSettings"]
            )
        )
    if "aribSourceSettings" in data:
        import capo_medialive.types.arib_source_settings

        out["arib_source_settings"] = (
            capo_medialive.types.arib_source_settings.deserialize_json(
                data["aribSourceSettings"]
            )
        )
    if "dvbSubSourceSettings" in data:
        import capo_medialive.types.dvb_sub_source_settings

        out["dvb_sub_source_settings"] = (
            capo_medialive.types.dvb_sub_source_settings.deserialize_json(
                data["dvbSubSourceSettings"]
            )
        )
    if "embeddedSourceSettings" in data:
        import capo_medialive.types.embedded_source_settings

        out["embedded_source_settings"] = (
            capo_medialive.types.embedded_source_settings.deserialize_json(
                data["embeddedSourceSettings"]
            )
        )
    if "scte20SourceSettings" in data:
        import capo_medialive.types.scte20_source_settings

        out["scte20_source_settings"] = (
            capo_medialive.types.scte20_source_settings.deserialize_json(
                data["scte20SourceSettings"]
            )
        )
    if "scte27SourceSettings" in data:
        import capo_medialive.types.scte27_source_settings

        out["scte27_source_settings"] = (
            capo_medialive.types.scte27_source_settings.deserialize_json(
                data["scte27SourceSettings"]
            )
        )
    if "teletextSourceSettings" in data:
        import capo_medialive.types.teletext_source_settings

        out["teletext_source_settings"] = (
            capo_medialive.types.teletext_source_settings.deserialize_json(
                data["teletextSourceSettings"]
            )
        )
    if "smartSubtitleSourceSettings" in data:
        import capo_medialive.types.smart_subtitle_source_settings

        out["smart_subtitle_source_settings"] = (
            capo_medialive.types.smart_subtitle_source_settings.deserialize_json(
                data["smartSubtitleSourceSettings"]
            )
        )
    return out
