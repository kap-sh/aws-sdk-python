"""Generated from Smithy shape ``com.amazonaws.connect#ReplicateInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.instance_id


class ReplicateInstanceResponse(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the replicated instance. You can find the <code>instanceId</code> in the ARN of the instance. The replicated instance has the same identifier as the instance it was replicated from.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the replicated instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReplicateInstanceResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> ReplicateInstanceResponse:
    out: ReplicateInstanceResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
