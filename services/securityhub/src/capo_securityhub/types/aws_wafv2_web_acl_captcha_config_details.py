"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2WebAclCaptchaConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details


class AwsWafv2WebAclCaptchaConfigDetails(TypedDict, closed=True):
    immunity_time_property: NotRequired[
        "capo_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details.AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails"
    ]
    """<p> Determines how long a CAPTCHA timestamp in the token remains valid after the client successfully solves a CAPTCHA puzzle. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2WebAclCaptchaConfigDetails) -> dict:
    out: dict = {}
    if "immunity_time_property" in value:
        import capo_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details

        out["ImmunityTimeProperty"] = (
            capo_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details.serialize_json(
                value["immunity_time_property"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2WebAclCaptchaConfigDetails:
    out: AwsWafv2WebAclCaptchaConfigDetails = {}  # type: ignore[typeddict-item]
    if "ImmunityTimeProperty" in data:
        import capo_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details

        out["immunity_time_property"] = (
            capo_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details.deserialize_json(
                data["ImmunityTimeProperty"]
            )
        )
    return out
