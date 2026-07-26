"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbv2LoadBalancerAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsElbv2LoadBalancerAttribute(TypedDict, closed=True):
    key: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the load balancer attribute.</p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
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
