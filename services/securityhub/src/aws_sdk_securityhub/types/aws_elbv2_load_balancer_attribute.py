"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbv2LoadBalancerAttribute``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbv2LoadBalancerAttribute(TypedDict):
    key: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the load balancer attribute.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the load balancer attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbv2LoadBalancerAttribute) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsElbv2LoadBalancerAttribute:
    out: AwsElbv2LoadBalancerAttribute = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
