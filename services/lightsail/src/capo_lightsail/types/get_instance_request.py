"""Generated from Smithy shape ``com.amazonaws.lightsail#GetInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class GetInstanceRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetInstanceRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetInstanceRequest:
    out: GetInstanceRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("GetInstanceRequest.instance_name required")
    return out
