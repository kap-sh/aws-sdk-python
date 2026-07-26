"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35TimeSignalApos``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min_negative1000_max1000
    import capo_medialive.types.scte35_apos_no_regional_blackout_behavior
    import capo_medialive.types.scte35_apos_web_delivery_allowed_behavior


class Scte35TimeSignalApos(TypedDict, closed=True):
    ad_avail_offset: NotRequired[
        "capo_medialive.types.__integer_min_negative1000_max1000.__integerMinNegative1000Max1000"
    ]
    """When specified, this offset (in milliseconds) is added to the input Ad Avail PTS time. This only applies to embedded SCTE 104/35 messages and does not apply to OOB messages."""
    no_regional_blackout_flag: NotRequired[
        "capo_medialive.types.scte35_apos_no_regional_blackout_behavior.Scte35AposNoRegionalBlackoutBehavior"
    ]
    """When set to ignore, Segment Descriptors with noRegionalBlackoutFlag set to 0 will no longer trigger blackouts or Ad Avail slates"""
    web_delivery_allowed_flag: NotRequired[
        "capo_medialive.types.scte35_apos_web_delivery_allowed_behavior.Scte35AposWebDeliveryAllowedBehavior"
    ]
    """When set to ignore, Segment Descriptors with webDeliveryAllowedFlag set to 0 will no longer trigger blackouts or Ad Avail slates"""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35TimeSignalApos) -> dict:
    out: dict = {}
    if "ad_avail_offset" in value:
        out["adAvailOffset"] = value["ad_avail_offset"]
    if "no_regional_blackout_flag" in value:
        import capo_medialive.types.scte35_apos_no_regional_blackout_behavior

        out["noRegionalBlackoutFlag"] = (
            capo_medialive.types.scte35_apos_no_regional_blackout_behavior.serialize_json(
                value["no_regional_blackout_flag"]
            )
        )
    if "web_delivery_allowed_flag" in value:
        import capo_medialive.types.scte35_apos_web_delivery_allowed_behavior

        out["webDeliveryAllowedFlag"] = (
            capo_medialive.types.scte35_apos_web_delivery_allowed_behavior.serialize_json(
                value["web_delivery_allowed_flag"]
            )
        )
    return out


def deserialize_json(data: dict) -> Scte35TimeSignalApos:
    out: Scte35TimeSignalApos = {}  # type: ignore[typeddict-item]
    if "adAvailOffset" in data:
        out["ad_avail_offset"] = data["adAvailOffset"]
    if "noRegionalBlackoutFlag" in data:
        import capo_medialive.types.scte35_apos_no_regional_blackout_behavior

        out["no_regional_blackout_flag"] = (
            capo_medialive.types.scte35_apos_no_regional_blackout_behavior.deserialize_json(
                data["noRegionalBlackoutFlag"]
            )
        )
    if "webDeliveryAllowedFlag" in data:
        import capo_medialive.types.scte35_apos_web_delivery_allowed_behavior

        out["web_delivery_allowed_flag"] = (
            capo_medialive.types.scte35_apos_web_delivery_allowed_behavior.deserialize_json(
                data["webDeliveryAllowedFlag"]
            )
        )
    return out
