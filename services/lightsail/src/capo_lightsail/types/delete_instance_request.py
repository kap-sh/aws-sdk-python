"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lightsail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.resource_name


class DeleteInstanceRequest(TypedDict, closed=True):
    instance_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the instance to delete.</p>"""
    force_delete_add_ons: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value to indicate whether to delete all add-ons for the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteInstanceRequest) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    if "force_delete_add_ons" in value:
        out["forceDeleteAddOns"] = value["force_delete_add_ons"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteInstanceRequest:
    out: DeleteInstanceRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    else:
        raise DeserializationError("DeleteInstanceRequest.instance_name required")
    if "forceDeleteAddOns" in data:
        out["force_delete_add_ons"] = data["forceDeleteAddOns"]
    return out
