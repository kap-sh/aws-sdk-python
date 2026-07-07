"""Generated from Smithy shape ``com.amazonaws.connect#AssociateInstanceStorageConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.association_id


class AssociateInstanceStorageConfigResponse(TypedDict, closed=True):
    association_id: NotRequired["aws_sdk_connect.types.association_id.AssociationId"]
    """<p>The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateInstanceStorageConfigResponse) -> dict:
    out: dict = {}
    if "association_id" in value:
        out["AssociationId"] = value["association_id"]
    return out


def deserialize_json(data: dict) -> AssociateInstanceStorageConfigResponse:
    out: AssociateInstanceStorageConfigResponse = {}  # type: ignore[typeddict-item]
    if "AssociationId" in data:
        out["association_id"] = data["AssociationId"]
    return out
