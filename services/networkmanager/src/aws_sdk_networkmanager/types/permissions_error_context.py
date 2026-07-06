"""Generated from Smithy shape ``com.amazonaws.networkmanager#PermissionsErrorContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.server_side_string


class PermissionsErrorContext(TypedDict, closed=True):
    missing_permission: NotRequired[
        "aws_sdk_networkmanager.types.server_side_string.ServerSideString"
    ]
    """<p>The missing permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionsErrorContext) -> dict:
    out: dict = {}
    if "missing_permission" in value:
        out["MissingPermission"] = value["missing_permission"]
    return out


def deserialize_json(data: dict) -> PermissionsErrorContext:
    out: PermissionsErrorContext = {}  # type: ignore[typeddict-item]
    if "MissingPermission" in data:
        out["missing_permission"] = data["MissingPermission"]
    return out
