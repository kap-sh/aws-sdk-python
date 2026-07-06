"""Generated from Smithy shape ``com.amazonaws.repostspace#DeregisterAdminInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_repostspace.types.admin_id
    import aws_sdk_repostspace.types.space_id


class DeregisterAdminInput(TypedDict, closed=True):
    space_id: "aws_sdk_repostspace.types.space_id.SpaceId"
    """<p>The ID of the private re:Post to remove the admin from.</p>"""
    admin_id: "aws_sdk_repostspace.types.admin_id.AdminId"
    """<p>The ID of the admin to remove.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterAdminInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterAdminInput:
    out: DeregisterAdminInput = {}  # type: ignore[typeddict-item]
    return out
