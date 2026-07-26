"""Generated from Smithy shape ``com.amazonaws.ivs#UpdatePlaybackRestrictionPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivs.types.playback_restriction_policy_allowed_country_list
    import capo_ivs.types.playback_restriction_policy_allowed_origin_list
    import capo_ivs.types.playback_restriction_policy_arn
    import capo_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement
    import capo_ivs.types.playback_restriction_policy_name


class UpdatePlaybackRestrictionPolicyRequest(TypedDict, closed=True):
    arn: "capo_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn"
    """<p>ARN of the playback-restriction-policy to be updated.</p>"""
    allowed_countries: NotRequired[
        "capo_ivs.types.playback_restriction_policy_allowed_country_list.PlaybackRestrictionPolicyAllowedCountryList"
    ]
    r"""<p>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a> codes. Default: All countries (an empty array).</p>"""
    allowed_origins: NotRequired[
        "capo_ivs.types.playback_restriction_policy_allowed_origin_list.PlaybackRestrictionPolicyAllowedOriginList"
    ]
    r"""<p>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin\">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</a>. Default: All origins (an empty array).</p>"""
    enable_strict_origin_enforcement: NotRequired[
        "capo_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement.PlaybackRestrictionPolicyEnableStrictOriginEnforcement"
    ]
    """<p>Whether channel playback is constrained by origin site. Default: <code>false</code>.</p>"""
    name: NotRequired[
        "capo_ivs.types.playback_restriction_policy_name.PlaybackRestrictionPolicyName"
    ]
    """<p>Playback-restriction-policy name. The value does not need to be unique.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePlaybackRestrictionPolicyRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "allowed_countries" in value:
        import capo_ivs.types.playback_restriction_policy_allowed_country_list

        out["allowedCountries"] = (
            capo_ivs.types.playback_restriction_policy_allowed_country_list.serialize_json(
                value["allowed_countries"]
            )
        )
    if "allowed_origins" in value:
        import capo_ivs.types.playback_restriction_policy_allowed_origin_list

        out["allowedOrigins"] = (
            capo_ivs.types.playback_restriction_policy_allowed_origin_list.serialize_json(
                value["allowed_origins"]
            )
        )
    if "enable_strict_origin_enforcement" in value:
        out["enableStrictOriginEnforcement"] = value["enable_strict_origin_enforcement"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdatePlaybackRestrictionPolicyRequest:
    out: UpdatePlaybackRestrictionPolicyRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError(
            "UpdatePlaybackRestrictionPolicyRequest.arn required"
        )
    if "allowedCountries" in data:
        import capo_ivs.types.playback_restriction_policy_allowed_country_list

        out["allowed_countries"] = (
            capo_ivs.types.playback_restriction_policy_allowed_country_list.deserialize_json(
                data["allowedCountries"]
            )
        )
    if "allowedOrigins" in data:
        import capo_ivs.types.playback_restriction_policy_allowed_origin_list

        out["allowed_origins"] = (
            capo_ivs.types.playback_restriction_policy_allowed_origin_list.deserialize_json(
                data["allowedOrigins"]
            )
        )
    if "enableStrictOriginEnforcement" in data:
        out["enable_strict_origin_enforcement"] = data["enableStrictOriginEnforcement"]
    if "name" in data:
        out["name"] = data["name"]
    return out
