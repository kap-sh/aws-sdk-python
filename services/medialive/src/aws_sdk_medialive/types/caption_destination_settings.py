"""Generated from Smithy shape ``com.amazonaws.medialive#CaptionDestinationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.arib_destination_settings
    import aws_sdk_medialive.types.burn_in_destination_settings
    import aws_sdk_medialive.types.dvb_sub_destination_settings
    import aws_sdk_medialive.types.ebu_tt_d_destination_settings
    import aws_sdk_medialive.types.embedded_destination_settings
    import aws_sdk_medialive.types.embedded_plus_scte20_destination_settings
    import aws_sdk_medialive.types.rtmp_caption_info_destination_settings
    import aws_sdk_medialive.types.scte20_plus_embedded_destination_settings
    import aws_sdk_medialive.types.scte27_destination_settings
    import aws_sdk_medialive.types.smpte_tt_destination_settings
    import aws_sdk_medialive.types.teletext_destination_settings
    import aws_sdk_medialive.types.ttml_destination_settings
    import aws_sdk_medialive.types.webvtt_destination_settings


class CaptionDestinationSettings(TypedDict, closed=True):
    arib_destination_settings: NotRequired[
        "aws_sdk_medialive.types.arib_destination_settings.AribDestinationSettings"
    ]
    burn_in_destination_settings: NotRequired[
        "aws_sdk_medialive.types.burn_in_destination_settings.BurnInDestinationSettings"
    ]
    dvb_sub_destination_settings: NotRequired[
        "aws_sdk_medialive.types.dvb_sub_destination_settings.DvbSubDestinationSettings"
    ]
    ebu_tt_d_destination_settings: NotRequired[
        "aws_sdk_medialive.types.ebu_tt_d_destination_settings.EbuTtDDestinationSettings"
    ]
    embedded_destination_settings: NotRequired[
        "aws_sdk_medialive.types.embedded_destination_settings.EmbeddedDestinationSettings"
    ]
    embedded_plus_scte20_destination_settings: NotRequired[
        "aws_sdk_medialive.types.embedded_plus_scte20_destination_settings.EmbeddedPlusScte20DestinationSettings"
    ]
    rtmp_caption_info_destination_settings: NotRequired[
        "aws_sdk_medialive.types.rtmp_caption_info_destination_settings.RtmpCaptionInfoDestinationSettings"
    ]
    scte20_plus_embedded_destination_settings: NotRequired[
        "aws_sdk_medialive.types.scte20_plus_embedded_destination_settings.Scte20PlusEmbeddedDestinationSettings"
    ]
    scte27_destination_settings: NotRequired[
        "aws_sdk_medialive.types.scte27_destination_settings.Scte27DestinationSettings"
    ]
    smpte_tt_destination_settings: NotRequired[
        "aws_sdk_medialive.types.smpte_tt_destination_settings.SmpteTtDestinationSettings"
    ]
    teletext_destination_settings: NotRequired[
        "aws_sdk_medialive.types.teletext_destination_settings.TeletextDestinationSettings"
    ]
    ttml_destination_settings: NotRequired[
        "aws_sdk_medialive.types.ttml_destination_settings.TtmlDestinationSettings"
    ]
    webvtt_destination_settings: NotRequired[
        "aws_sdk_medialive.types.webvtt_destination_settings.WebvttDestinationSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CaptionDestinationSettings) -> dict:
    out: dict = {}
    if "arib_destination_settings" in value:
        import aws_sdk_medialive.types.arib_destination_settings

        out["aribDestinationSettings"] = (
            aws_sdk_medialive.types.arib_destination_settings.serialize_json(
                value["arib_destination_settings"]
            )
        )
    if "burn_in_destination_settings" in value:
        import aws_sdk_medialive.types.burn_in_destination_settings

        out["burnInDestinationSettings"] = (
            aws_sdk_medialive.types.burn_in_destination_settings.serialize_json(
                value["burn_in_destination_settings"]
            )
        )
    if "dvb_sub_destination_settings" in value:
        import aws_sdk_medialive.types.dvb_sub_destination_settings

        out["dvbSubDestinationSettings"] = (
            aws_sdk_medialive.types.dvb_sub_destination_settings.serialize_json(
                value["dvb_sub_destination_settings"]
            )
        )
    if "ebu_tt_d_destination_settings" in value:
        import aws_sdk_medialive.types.ebu_tt_d_destination_settings

        out["ebuTtDDestinationSettings"] = (
            aws_sdk_medialive.types.ebu_tt_d_destination_settings.serialize_json(
                value["ebu_tt_d_destination_settings"]
            )
        )
    if "embedded_destination_settings" in value:
        import aws_sdk_medialive.types.embedded_destination_settings

        out["embeddedDestinationSettings"] = (
            aws_sdk_medialive.types.embedded_destination_settings.serialize_json(
                value["embedded_destination_settings"]
            )
        )
    if "embedded_plus_scte20_destination_settings" in value:
        import aws_sdk_medialive.types.embedded_plus_scte20_destination_settings

        out["embeddedPlusScte20DestinationSettings"] = (
            aws_sdk_medialive.types.embedded_plus_scte20_destination_settings.serialize_json(
                value["embedded_plus_scte20_destination_settings"]
            )
        )
    if "rtmp_caption_info_destination_settings" in value:
        import aws_sdk_medialive.types.rtmp_caption_info_destination_settings

        out["rtmpCaptionInfoDestinationSettings"] = (
            aws_sdk_medialive.types.rtmp_caption_info_destination_settings.serialize_json(
                value["rtmp_caption_info_destination_settings"]
            )
        )
    if "scte20_plus_embedded_destination_settings" in value:
        import aws_sdk_medialive.types.scte20_plus_embedded_destination_settings

        out["scte20PlusEmbeddedDestinationSettings"] = (
            aws_sdk_medialive.types.scte20_plus_embedded_destination_settings.serialize_json(
                value["scte20_plus_embedded_destination_settings"]
            )
        )
    if "scte27_destination_settings" in value:
        import aws_sdk_medialive.types.scte27_destination_settings

        out["scte27DestinationSettings"] = (
            aws_sdk_medialive.types.scte27_destination_settings.serialize_json(
                value["scte27_destination_settings"]
            )
        )
    if "smpte_tt_destination_settings" in value:
        import aws_sdk_medialive.types.smpte_tt_destination_settings

        out["smpteTtDestinationSettings"] = (
            aws_sdk_medialive.types.smpte_tt_destination_settings.serialize_json(
                value["smpte_tt_destination_settings"]
            )
        )
    if "teletext_destination_settings" in value:
        import aws_sdk_medialive.types.teletext_destination_settings

        out["teletextDestinationSettings"] = (
            aws_sdk_medialive.types.teletext_destination_settings.serialize_json(
                value["teletext_destination_settings"]
            )
        )
    if "ttml_destination_settings" in value:
        import aws_sdk_medialive.types.ttml_destination_settings

        out["ttmlDestinationSettings"] = (
            aws_sdk_medialive.types.ttml_destination_settings.serialize_json(
                value["ttml_destination_settings"]
            )
        )
    if "webvtt_destination_settings" in value:
        import aws_sdk_medialive.types.webvtt_destination_settings

        out["webvttDestinationSettings"] = (
            aws_sdk_medialive.types.webvtt_destination_settings.serialize_json(
                value["webvtt_destination_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> CaptionDestinationSettings:
    out: CaptionDestinationSettings = {}  # type: ignore[typeddict-item]
    if "aribDestinationSettings" in data:
        import aws_sdk_medialive.types.arib_destination_settings

        out["arib_destination_settings"] = (
            aws_sdk_medialive.types.arib_destination_settings.deserialize_json(
                data["aribDestinationSettings"]
            )
        )
    if "burnInDestinationSettings" in data:
        import aws_sdk_medialive.types.burn_in_destination_settings

        out["burn_in_destination_settings"] = (
            aws_sdk_medialive.types.burn_in_destination_settings.deserialize_json(
                data["burnInDestinationSettings"]
            )
        )
    if "dvbSubDestinationSettings" in data:
        import aws_sdk_medialive.types.dvb_sub_destination_settings

        out["dvb_sub_destination_settings"] = (
            aws_sdk_medialive.types.dvb_sub_destination_settings.deserialize_json(
                data["dvbSubDestinationSettings"]
            )
        )
    if "ebuTtDDestinationSettings" in data:
        import aws_sdk_medialive.types.ebu_tt_d_destination_settings

        out["ebu_tt_d_destination_settings"] = (
            aws_sdk_medialive.types.ebu_tt_d_destination_settings.deserialize_json(
                data["ebuTtDDestinationSettings"]
            )
        )
    if "embeddedDestinationSettings" in data:
        import aws_sdk_medialive.types.embedded_destination_settings

        out["embedded_destination_settings"] = (
            aws_sdk_medialive.types.embedded_destination_settings.deserialize_json(
                data["embeddedDestinationSettings"]
            )
        )
    if "embeddedPlusScte20DestinationSettings" in data:
        import aws_sdk_medialive.types.embedded_plus_scte20_destination_settings

        out["embedded_plus_scte20_destination_settings"] = (
            aws_sdk_medialive.types.embedded_plus_scte20_destination_settings.deserialize_json(
                data["embeddedPlusScte20DestinationSettings"]
            )
        )
    if "rtmpCaptionInfoDestinationSettings" in data:
        import aws_sdk_medialive.types.rtmp_caption_info_destination_settings

        out["rtmp_caption_info_destination_settings"] = (
            aws_sdk_medialive.types.rtmp_caption_info_destination_settings.deserialize_json(
                data["rtmpCaptionInfoDestinationSettings"]
            )
        )
    if "scte20PlusEmbeddedDestinationSettings" in data:
        import aws_sdk_medialive.types.scte20_plus_embedded_destination_settings

        out["scte20_plus_embedded_destination_settings"] = (
            aws_sdk_medialive.types.scte20_plus_embedded_destination_settings.deserialize_json(
                data["scte20PlusEmbeddedDestinationSettings"]
            )
        )
    if "scte27DestinationSettings" in data:
        import aws_sdk_medialive.types.scte27_destination_settings

        out["scte27_destination_settings"] = (
            aws_sdk_medialive.types.scte27_destination_settings.deserialize_json(
                data["scte27DestinationSettings"]
            )
        )
    if "smpteTtDestinationSettings" in data:
        import aws_sdk_medialive.types.smpte_tt_destination_settings

        out["smpte_tt_destination_settings"] = (
            aws_sdk_medialive.types.smpte_tt_destination_settings.deserialize_json(
                data["smpteTtDestinationSettings"]
            )
        )
    if "teletextDestinationSettings" in data:
        import aws_sdk_medialive.types.teletext_destination_settings

        out["teletext_destination_settings"] = (
            aws_sdk_medialive.types.teletext_destination_settings.deserialize_json(
                data["teletextDestinationSettings"]
            )
        )
    if "ttmlDestinationSettings" in data:
        import aws_sdk_medialive.types.ttml_destination_settings

        out["ttml_destination_settings"] = (
            aws_sdk_medialive.types.ttml_destination_settings.deserialize_json(
                data["ttmlDestinationSettings"]
            )
        )
    if "webvttDestinationSettings" in data:
        import aws_sdk_medialive.types.webvtt_destination_settings

        out["webvtt_destination_settings"] = (
            aws_sdk_medialive.types.webvtt_destination_settings.deserialize_json(
                data["webvttDestinationSettings"]
            )
        )
    return out
