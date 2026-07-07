"""Generated from Smithy shape ``com.amazonaws.finspacedata#DisassociateUserFromPermissionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace_data.types.status_code


class DisassociateUserFromPermissionGroupResponse(TypedDict, closed=True):
    status_code: "aws_sdk_finspace_data.types.status_code.StatusCode"
    """<p>The returned status code of the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateUserFromPermissionGroupResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateUserFromPermissionGroupResponse:
    out: DisassociateUserFromPermissionGroupResponse = {}  # type: ignore[typeddict-item]
    return out
