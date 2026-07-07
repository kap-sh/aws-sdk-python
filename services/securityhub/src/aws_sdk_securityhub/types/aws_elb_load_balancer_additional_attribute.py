"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerAdditionalAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbLoadBalancerAdditionalAttribute(TypedDict, closed=True):
    key: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the attribute.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerAdditionalAttribute) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerAdditionalAttribute:
    out: AwsElbLoadBalancerAdditionalAttribute = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
