"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbAppCookieStickinessPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_app_cookie_stickiness_policy

AwsElbAppCookieStickinessPolicies: TypeAlias = list[
    "capo_securityhub.types.aws_elb_app_cookie_stickiness_policy.AwsElbAppCookieStickinessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbAppCookieStickinessPolicies) -> list:
    import capo_securityhub.types.aws_elb_app_cookie_stickiness_policy

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_elb_app_cookie_stickiness_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbAppCookieStickinessPolicies:
    import capo_securityhub.types.aws_elb_app_cookie_stickiness_policy

    out: AwsElbAppCookieStickinessPolicies = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_elb_app_cookie_stickiness_policy.deserialize_json(
                item
            )
        )
    return out
