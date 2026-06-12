"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbAppCookieStickinessPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbAppCookieStickinessPolicy(TypedDict):
    cookie_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the application cookie used for stickiness.</p>"""
    policy_name: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The mnemonic name for the policy being created. The name must be unique within the set of policies for the load balancer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbAppCookieStickinessPolicy) -> dict:
    out: dict = {}
    if "cookie_name" in value:
        out["CookieName"] = value["cookie_name"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    return out


def deserialize_json(data: dict) -> AwsElbAppCookieStickinessPolicy:
    out: AwsElbAppCookieStickinessPolicy = {}  # type: ignore[typeddict-item]
    if "CookieName" in data:
        out["cookie_name"] = data["CookieName"]
    if "PolicyName" in data:
        out["policy_name"] = data["PolicyName"]
    return out
