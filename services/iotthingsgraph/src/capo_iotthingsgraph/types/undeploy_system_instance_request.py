"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#UndeploySystemInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.urn


class UndeploySystemInstanceRequest(TypedDict, closed=True):
    id: NotRequired["capo_iotthingsgraph.types.urn.Urn"]
    """<p>The ID of the system instance to remove from its target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UndeploySystemInstanceRequest) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UndeploySystemInstanceRequest:
    out: UndeploySystemInstanceRequest = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    return out
