"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbAppCookieStickinessPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policy

AwsElbAppCookieStickinessPolicies: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policy.AwsElbAppCookieStickinessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbAppCookieStickinessPolicies) -> list:
    import aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbAppCookieStickinessPolicies:
    import aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policy

    out: AwsElbAppCookieStickinessPolicies = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policy.deserialize_json(
                item
            )
        )
    return out
