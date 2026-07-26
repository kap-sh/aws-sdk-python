"""Generated from Smithy shape ``com.amazonaws.ram#GetPermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.resource_share_permission_detail


class GetPermissionResponse(TypedDict, closed=True):
    permission: NotRequired[
        "capo_ram.types.resource_share_permission_detail.ResourceSharePermissionDetail"
    ]
    """<p>An object with details about the permission.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPermissionResponse) -> dict:
    out: dict = {}
    if "permission" in value:
        import capo_ram.types.resource_share_permission_detail

        out["permission"] = (
            capo_ram.types.resource_share_permission_detail.serialize_json(
                value["permission"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetPermissionResponse:
    out: GetPermissionResponse = {}  # type: ignore[typeddict-item]
    if "permission" in data:
        import capo_ram.types.resource_share_permission_detail

        out["permission"] = (
            capo_ram.types.resource_share_permission_detail.deserialize_json(
                data["permission"]
            )
        )
    return out
