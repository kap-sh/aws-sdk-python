"""Generated from Smithy shape ``com.amazonaws.ram#CreatePermissionVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.resource_share_permission_detail
    import aws_sdk_ram.types.string


class CreatePermissionVersionResponse(TypedDict):
    permission: NotRequired[
        "aws_sdk_ram.types.resource_share_permission_detail.ResourceSharePermissionDetail"
    ]
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePermissionVersionResponse) -> dict:
    out: dict = {}
    if "permission" in value:
        import aws_sdk_ram.types.resource_share_permission_detail

        out["permission"] = (
            aws_sdk_ram.types.resource_share_permission_detail.serialize_json(
                value["permission"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePermissionVersionResponse:
    out: CreatePermissionVersionResponse = {}  # type: ignore[typeddict-item]
    if "permission" in data:
        import aws_sdk_ram.types.resource_share_permission_detail

        out["permission"] = (
            aws_sdk_ram.types.resource_share_permission_detail.deserialize_json(
                data["permission"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
