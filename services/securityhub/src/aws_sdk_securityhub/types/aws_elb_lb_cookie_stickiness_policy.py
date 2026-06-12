"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLbCookieStickinessPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbLbCookieStickinessPolicy(TypedDict):
    cookie_expiration_period: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The amount of time, in seconds, after which the cookie is considered stale. If an expiration period is not specified, the stickiness session lasts for the duration of the browser session.</p>"""
    policy_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the policy. The name must be unique within the set of policies for the load balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLbCookieStickinessPolicy) -> dict:
    out: dict = {}
    if "cookie_expiration_period" in value:
        out["CookieExpirationPeriod"] = value["cookie_expiration_period"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_json(data: dict) -> AwsElbLbCookieStickinessPolicy:
    out: AwsElbLbCookieStickinessPolicy = {}  # type: ignore[typeddict-item]
    if "CookieExpirationPeriod" in data:
        out["cookie_expiration_period"] = data["CookieExpirationPeriod"]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    return out
