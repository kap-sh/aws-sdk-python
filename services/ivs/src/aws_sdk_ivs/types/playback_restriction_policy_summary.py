"""Generated from Smithy shape ``com.amazonaws.ivs#PlaybackRestrictionPolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list
    import aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list
    import aws_sdk_ivs.types.playback_restriction_policy_arn
    import aws_sdk_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement
    import aws_sdk_ivs.types.playback_restriction_policy_name
    import aws_sdk_ivs.types.tags


class PlaybackRestrictionPolicySummary(TypedDict, closed=True):
    arn: (
        "aws_sdk_ivs.types.playback_restriction_policy_arn.PlaybackRestrictionPolicyArn"
    )
    """<p>Playback-restriction-policy ARN</p>"""
    allowed_countries: "aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list.PlaybackRestrictionPolicyAllowedCountryList"
    r"""<p>A list of country codes that control geoblocking restriction. Allowed values are the officially assigned <a href=\"https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2</a> codes. Default: All countries (an empty array).</p>"""
    allowed_origins: "aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list.PlaybackRestrictionPolicyAllowedOriginList"
    r"""<p>A list of origin sites that control CORS restriction. Allowed values are the same as valid values of the Origin header defined at <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin\">https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin</a>. Default: All origins (an empty array).</p>"""
    enable_strict_origin_enforcement: NotRequired[
        "aws_sdk_ivs.types.playback_restriction_policy_enable_strict_origin_enforcement.PlaybackRestrictionPolicyEnableStrictOriginEnforcement"
    ]
    """<p>Whether channel playback is constrained by origin site. Default: <code>false</code>.</p>"""
    name: NotRequired[
        "aws_sdk_ivs.types.playback_restriction_policy_name.PlaybackRestrictionPolicyName"
    ]
    """<p>Playback-restriction-policy name. The value does not need to be unique.</p>"""
    tags: NotRequired["aws_sdk_ivs.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of 1-50 maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no service-specific constraints beyond what is documented there.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlaybackRestrictionPolicySummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list

    out["allowedCountries"] = (
        aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list.serialize_json(
            value["allowed_countries"]
        )
    )
    import aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list

    out["allowedOrigins"] = (
        aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list.serialize_json(
            value["allowed_origins"]
        )
    )
    if "enable_strict_origin_enforcement" in value:
        out["enableStrictOriginEnforcement"] = value["enable_strict_origin_enforcement"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PlaybackRestrictionPolicySummary:
    out: PlaybackRestrictionPolicySummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("PlaybackRestrictionPolicySummary.arn required")
    if "allowedCountries" in data:
        import aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list

        out["allowed_countries"] = (
            aws_sdk_ivs.types.playback_restriction_policy_allowed_country_list.deserialize_json(
                data["allowedCountries"]
            )
        )
    else:
        raise DeserializationError(
            "PlaybackRestrictionPolicySummary.allowed_countries required"
        )
    if "allowedOrigins" in data:
        import aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list

        out["allowed_origins"] = (
            aws_sdk_ivs.types.playback_restriction_policy_allowed_origin_list.deserialize_json(
                data["allowedOrigins"]
            )
        )
    else:
        raise DeserializationError(
            "PlaybackRestrictionPolicySummary.allowed_origins required"
        )
    if "enableStrictOriginEnforcement" in data:
        out["enable_strict_origin_enforcement"] = data["enableStrictOriginEnforcement"]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_ivs.types.tags

        out["tags"] = aws_sdk_ivs.types.tags.deserialize_json(data["tags"])
    return out
