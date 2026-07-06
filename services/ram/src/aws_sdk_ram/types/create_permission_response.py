"""Generated from Smithy shape ``com.amazonaws.ram#CreatePermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share_permission_summary
    import aws_sdk_ram.types.string


class CreatePermissionResponse(TypedDict, closed=True):
    permission: NotRequired[
        "aws_sdk_ram.types.resource_share_permission_summary.ResourceSharePermissionSummary"
    ]
    """<p>A structure with information about this customer managed permission.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePermissionResponse) -> dict:
    out: dict = {}
    if "permission" in value:
        import aws_sdk_ram.types.resource_share_permission_summary

        out["permission"] = (
            aws_sdk_ram.types.resource_share_permission_summary.serialize_json(
                value["permission"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePermissionResponse:
    out: CreatePermissionResponse = {}  # type: ignore[typeddict-item]
    if "permission" in data:
        import aws_sdk_ram.types.resource_share_permission_summary

        out["permission"] = (
            aws_sdk_ram.types.resource_share_permission_summary.deserialize_json(
                data["permission"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
