"""Generated from Smithy shape ``com.amazonaws.greengrassv2#GetServiceRoleForAccountResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_greengrassv2.types.string


class GetServiceRoleForAccountResponse(TypedDict):
    associated_at: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>The time when the service role was associated with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region.</p>"""
    role_arn: NotRequired["aws_sdk_greengrassv2.types.string.String"]
    """<p>The ARN of the service role that is associated with IoT Greengrass for your Amazon Web Services account in this Amazon Web Services Region.</p>"""


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
