"""Generated from Smithy shape ``com.amazonaws.greengrass#GetAssociatedRoleResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetAssociatedRoleResponse(TypedDict):
    associated_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time when the role was associated with the group."""
    role_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the role that is associated with the group."""


# --- restJson1 ser/de ---
def serialize_json(value: GetAssociatedRoleResponse) -> dict:
    out: dict = {}
    if "associated_at" in value:
        out["AssociatedAt"] = value["associated_at"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> GetAssociatedRoleResponse:
    out: GetAssociatedRoleResponse = {}  # type: ignore[typeddict-item]
    if "AssociatedAt" in data:
        out["associated_at"] = data["AssociatedAt"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
