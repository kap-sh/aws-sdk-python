"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long


class AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails(TypedDict):
    immunity_time: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p> The amount of time, in seconds, that a CAPTCHA or challenge timestamp is considered valid by WAF. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails,
) -> dict:
    out: dict = {}
    if "immunity_time" in value:
        out["ImmunityTime"] = value["immunity_time"]
    return out


def deserialize_json(
    data: dict,
) -> AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails:
    out: AwsWafv2WebAclCaptchaConfigImmunityTimePropertyDetails = {}  # type: ignore[typeddict-item]
    if "ImmunityTime" in data:
        out["immunity_time"] = data["ImmunityTime"]
    return out
