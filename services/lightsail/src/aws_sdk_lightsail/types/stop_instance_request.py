"""Generated from Smithy shape ``com.amazonaws.lightsail#StopInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.resource_name


class StopInstanceRequest(TypedDict, closed=True):
    instance_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance (a virtual private server) to stop.</p>"""
    force: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>When set to <code>True</code>, forces a Lightsail instance that is stuck in a <code>stopping</code> state to stop.</p> <important> <p>Only use the <code>force</code> parameter if your instance is stuck in the <code>stopping</code> state. In any other state, your instance should stop normally without adding this parameter to your API request.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopInstanceRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopInstanceRequest:
    out: StopInstanceRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("StopInstanceRequest.instance_name required")
    if "force" in data:
        out["force"] = data["force"]
    return out
