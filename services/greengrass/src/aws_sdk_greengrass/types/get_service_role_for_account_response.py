"""Generated from Smithy shape ``com.amazonaws.greengrass#GetServiceRoleForAccountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__string


class GetServiceRoleForAccountResponse(TypedDict, closed=True):
    associated_at: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The time when the service role was associated with the account."""
    role_arn: NotRequired["aws_sdk_greengrass.types.__string.__string"]
    """The ARN of the role which is associated with the account."""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceRoleForAccountResponse) -> dict:
    out: dict = {}
    if "associated_at" in value:
        out["AssociatedAt"] = value["associated_at"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> GetServiceRoleForAccountResponse:
    out: GetServiceRoleForAccountResponse = {}  # type: ignore[typeddict-item]
    if "AssociatedAt" in data:
        out["associated_at"] = data["AssociatedAt"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
