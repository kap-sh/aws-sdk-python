"""Generated from Smithy shape ``com.amazonaws.greengrass#AssociateRoleToGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class AssociateRoleToGroupResponse(TypedDict):
    associated_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time, in milliseconds since the epoch, when the role ARN was associated with the group."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateRoleToGroupResponse) -> dict:
    out: dict = {}
    if "associated_at" in value:
        out["AssociatedAt"] = value["associated_at"]
    return out


def deserialize_json(data: dict) -> AssociateRoleToGroupResponse:
    out: AssociateRoleToGroupResponse = {}  # type: ignore[typeddict-item]
    if "AssociatedAt" in data:
        out["associated_at"] = data["AssociatedAt"]
    return out
