"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerInstance``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsElbLoadBalancerInstance(TypedDict):
    instance_id: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The instance identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerInstance) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_json(data: dict) -> AwsElbLoadBalancerInstance:
    out: AwsElbLoadBalancerInstance = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    return out
