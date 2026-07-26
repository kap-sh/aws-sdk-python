"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Termination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.calling_region_list
    import capo_chime_sdk_voice.types.cps_limit
    import capo_chime_sdk_voice.types.e164_phone_number
    import capo_chime_sdk_voice.types.string_list


class Termination(TypedDict, closed=True):
    cps_limit: NotRequired["capo_chime_sdk_voice.types.cps_limit.CpsLimit"]
    """<p>The limit on calls per second. Max value based on account service quota. Default value of 1.</p>"""
    default_phone_number: NotRequired[
        "capo_chime_sdk_voice.types.e164_phone_number.E164PhoneNumber"
    ]
    """<p>The default outbound calling number.</p>"""
    calling_regions: NotRequired[
        "capo_chime_sdk_voice.types.calling_region_list.CallingRegionList"
    ]
    """<p>The countries to which calls are allowed, in ISO 3166-1 alpha-2 format. Required.</p>"""
    cidr_allowed_list: NotRequired["capo_chime_sdk_voice.types.string_list.StringList"]
    """<p>The IP addresses allowed to make calls, in CIDR format.</p>"""
    disabled: NotRequired["capo_chime_sdk_voice.types.boolean.Boolean"]
    """<p>When termination is disabled, outbound calls cannot be made.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Termination) -> dict:
    out: dict = {}
    if "cps_limit" in value:
        out["CpsLimit"] = value["cps_limit"]
    if "default_phone_number" in value:
        out["DefaultPhoneNumber"] = value["default_phone_number"]
    if "calling_regions" in value:
        import capo_chime_sdk_voice.types.calling_region_list

        out["CallingRegions"] = (
            capo_chime_sdk_voice.types.calling_region_list.serialize_json(
                value["calling_regions"]
            )
        )
    if "cidr_allowed_list" in value:
        import capo_chime_sdk_voice.types.string_list

        out["CidrAllowedList"] = capo_chime_sdk_voice.types.string_list.serialize_json(
            value["cidr_allowed_list"]
        )
    if "disabled" in value:
        out["Disabled"] = value["disabled"]
    return out


def deserialize_json(data: dict) -> Termination:
    out: Termination = {}  # type: ignore[typeddict-item]
    if "CpsLimit" in data:
        out["cps_limit"] = data["CpsLimit"]
    if "DefaultPhoneNumber" in data:
        out["default_phone_number"] = data["DefaultPhoneNumber"]
    if "CallingRegions" in data:
        import capo_chime_sdk_voice.types.calling_region_list

        out["calling_regions"] = (
            capo_chime_sdk_voice.types.calling_region_list.deserialize_json(
                data["CallingRegions"]
            )
        )
    if "CidrAllowedList" in data:
        import capo_chime_sdk_voice.types.string_list

        out["cidr_allowed_list"] = (
            capo_chime_sdk_voice.types.string_list.deserialize_json(
                data["CidrAllowedList"]
            )
        )
    if "Disabled" in data:
        out["disabled"] = data["Disabled"]
    return out
