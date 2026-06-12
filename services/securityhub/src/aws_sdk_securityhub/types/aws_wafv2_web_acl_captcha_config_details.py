"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2WebAclCaptchaConfigDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details


class AwsWafv2WebAclCaptchaConfigDetails(TypedDict):
    immunity_time_property: NotRequired[
        "aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details.AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails"
    ]
    """<p> Determines how long a CAPTCHA timestamp in the token remains valid after the client successfully solves a CAPTCHA puzzle. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2WebAclCaptchaConfigDetails) -> dict:
    out: dict = {}
    if "immunity_time_property" in value:
        import aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details

        out["ImmunityTimeProperty"] = (
            aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details.serialize_json(
                value["immunity_time_property"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2WebAclCaptchaConfigDetails:
    out: AwsWafv2WebAclCaptchaConfigDetails = {}  # type: ignore[typeddict-item]
    if "ImmunityTimeProperty" in data:
        import aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details

        out["immunity_time_property"] = (
            aws_sdk_securityhub.types.aws_wafv2_web_acl_captcha_config_immunity_time_property_details.deserialize_json(
                data["ImmunityTimeProperty"]
            )
        )
    return out
