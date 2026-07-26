"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLbCookieStickinessPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_lb_cookie_stickiness_policy

AwsElbLbCookieStickinessPolicies: TypeAlias = list[
    "capo_securityhub.types.aws_elb_lb_cookie_stickiness_policy.AwsElbLbCookieStickinessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLbCookieStickinessPolicies) -> list:
    import capo_securityhub.types.aws_elb_lb_cookie_stickiness_policy

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_elb_lb_cookie_stickiness_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbLbCookieStickinessPolicies:
    import capo_securityhub.types.aws_elb_lb_cookie_stickiness_policy

    out: AwsElbLbCookieStickinessPolicies = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_elb_lb_cookie_stickiness_policy.deserialize_json(
                item
            )
        )
    return out
