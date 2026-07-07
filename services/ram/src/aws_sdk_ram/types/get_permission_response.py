"""Generated from Smithy shape ``com.amazonaws.ram#GetPermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share_permission_detail


class GetPermissionResponse(TypedDict, closed=True):
    permission: NotRequired[
        "aws_sdk_ram.types.resource_share_permission_detail.ResourceSharePermissionDetail"
    ]
    """<p>An object with details about the permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPermissionResponse) -> dict:
    out: dict = {}
    if "permission" in value:
        import aws_sdk_ram.types.resource_share_permission_detail

        out["permission"] = (
            aws_sdk_ram.types.resource_share_permission_detail.serialize_json(
                value["permission"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPermissionResponse:
    out: GetPermissionResponse = {}  # type: ignore[typeddict-item]
    if "permission" in data:
        import aws_sdk_ram.types.resource_share_permission_detail

        out["permission"] = (
            aws_sdk_ram.types.resource_share_permission_detail.deserialize_json(
                data["permission"]
            )
        )
    return out
