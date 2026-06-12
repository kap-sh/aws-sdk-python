"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerPolicies``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policies
    import aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policies
    import aws_sdk_securityhub.types.string_list


class AwsElbLoadBalancerPolicies(TypedDict):
    app_cookie_stickiness_policies: NotRequired[
        "aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policies.AwsElbAppCookieStickinessPolicies"
    ]
    """<p>The stickiness policies that are created using <code>CreateAppCookieStickinessPolicy</code>.</p>"""
    lb_cookie_stickiness_policies: NotRequired[
        "aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policies.AwsElbLbCookieStickinessPolicies"
    ]
    """<p>The stickiness policies that are created using <code>CreateLBCookieStickinessPolicy</code>.</p>"""
    other_policies: NotRequired["aws_sdk_securityhub.types.string_list.StringList"]
    """<p>The policies other than the stickiness policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerPolicies) -> dict:
    out: dict = {}
    if "app_cookie_stickiness_policies" in value:
        import aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policies

        out["AppCookieStickinessPolicies"] = (
            aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policies.serialize_json(
                value["app_cookie_stickiness_policies"]
            )
        )
    if "lb_cookie_stickiness_policies" in value:
        import aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policies

        out["LbCookieStickinessPolicies"] = (
            aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policies.serialize_json(
                value["lb_cookie_stickiness_policies"]
            )
        )
    if "other_policies" in value:
        import aws_sdk_securityhub.types.string_list

        out["OtherPolicies"] = aws_sdk_securityhub.types.string_list.serialize_json(
            value["other_policies"]
        )
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerPolicies:
    out: AwsElbLoadBalancerPolicies = {}  # type: ignore[typeddict-item]
    if "AppCookieStickinessPolicies" in data:
        import aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policies

        out["app_cookie_stickiness_policies"] = (
            aws_sdk_securityhub.types.aws_elb_app_cookie_stickiness_policies.deserialize_json(
                data["AppCookieStickinessPolicies"]
            )
        )
    if "LbCookieStickinessPolicies" in data:
        import aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policies

        out["lb_cookie_stickiness_policies"] = (
            aws_sdk_securityhub.types.aws_elb_lb_cookie_stickiness_policies.deserialize_json(
                data["LbCookieStickinessPolicies"]
            )
        )
    if "OtherPolicies" in data:
        import aws_sdk_securityhub.types.string_list

        out["other_policies"] = aws_sdk_securityhub.types.string_list.deserialize_json(
            data["OtherPolicies"]
        )
    return out
