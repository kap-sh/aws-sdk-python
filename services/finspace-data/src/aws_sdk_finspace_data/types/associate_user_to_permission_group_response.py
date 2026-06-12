"""Generated from Smithy shape ``com.amazonaws.finspacedata#AssociateUserToPermissionGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.status_code


class AssociateUserToPermissionGroupResponse(TypedDict):
    status_code: "aws_sdk_finspace_data.types.status_code.StatusCode"
    """<p>The returned status code of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserToPermissionGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateUserToPermissionGroupResponse:
    out: AssociateUserToPermissionGroupResponse = {}  # type: ignore[typeddict-item]
    return out
