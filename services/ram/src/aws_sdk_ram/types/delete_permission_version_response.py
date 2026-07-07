"""Generated from Smithy shape ``com.amazonaws.ram#DeletePermissionVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.permission_status
    import aws_sdk_ram.types.string


class DeletePermissionVersionResponse(TypedDict, closed=True):
    return_value: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>A boolean value that indicates whether the operation is successful.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""
    permission_status: NotRequired[
        "aws_sdk_ram.types.permission_status.PermissionStatus"
    ]
    """<p>This operation is performed asynchronously, and this response parameter indicates the current status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePermissionVersionResponse) -> dict:
    out: dict = {}
    if "return_value" in value:
        out["returnValue"] = value["return_value"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "permission_status" in value:
        import aws_sdk_ram.types.permission_status

        out["permissionStatus"] = aws_sdk_ram.types.permission_status.serialize_json(
            value["permission_status"]
        )
    return out


def deserialize_json(data: dict) -> DeletePermissionVersionResponse:
    out: DeletePermissionVersionResponse = {}  # type: ignore[typeddict-item]
    if "returnValue" in data:
        out["return_value"] = data["returnValue"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "permissionStatus" in data:
        import aws_sdk_ram.types.permission_status

        out["permission_status"] = aws_sdk_ram.types.permission_status.deserialize_json(
            data["permissionStatus"]
        )
    return out
