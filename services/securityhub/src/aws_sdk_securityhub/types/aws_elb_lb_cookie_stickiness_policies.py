"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLbCookieStickinessPolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policy

AwsElbLbCookieStickinessPolicies: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policy.AwsElbLbCookieStickinessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLbCookieStickinessPolicies) -> list:
    import aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policy.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbLbCookieStickinessPolicies:
    import aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policy

    out: AwsElbLbCookieStickinessPolicies = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policy.deserialize_json(
                item
            )
        )
    return out
