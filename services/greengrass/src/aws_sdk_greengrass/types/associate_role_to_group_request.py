"""Generated from Smithy shape ``com.amazonaws.greengrass#AssociateRoleToGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class AssociateRoleToGroupRequest(TypedDict):
    group_id: "aws_sdk_greengrass.types.__string.__string"
    """The ID of the Greengrass group."""
    role_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the role you wish to associate with this group. The existence of the role is not validated."""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateRoleToGroupRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> AssociateRoleToGroupRequest:
    out: AssociateRoleToGroupRequest = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
