"""Generated from Smithy shape ``com.amazonaws.ram#SetDefaultPermissionVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.string


class SetDefaultPermissionVersionResponse(TypedDict):
    return_value: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>A boolean value that indicates whether the operation was successful.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDefaultPermissionVersionResponse) -> dict:
    out: dict = {}
    if "return_value" in value:
        out["returnValue"] = value["return_value"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SetDefaultPermissionVersionResponse:
    out: SetDefaultPermissionVersionResponse = {}  # type: ignore[typeddict-item]
    if "returnValue" in data:
        out["return_value"] = data["returnValue"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
