"""Generated from Smithy shape ``com.amazonaws.ram#DeleteResourceShareResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ram.types.boolean
    import aws_sdk_ram.types.string


class DeleteResourceShareResponse(TypedDict, closed=True):
    return_value: NotRequired["aws_sdk_ram.types.boolean.Boolean"]
    """<p>A return value of <code>true</code> indicates that the request succeeded. A value of <code>false</code> indicates that the request failed.</p>"""
    client_token: NotRequired["aws_sdk_ram.types.string.String"]
    """<p>The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the <code>clientToken</code> request parameter of that later call. All other parameters must also have the same values that you used in the first call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteResourceShareResponse) -> dict:
    out: dict = {}
    if "return_value" in value:
        out["returnValue"] = value["return_value"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DeleteResourceShareResponse:
    out: DeleteResourceShareResponse = {}  # type: ignore[typeddict-item]
    if "returnValue" in data:
        out["return_value"] = data["returnValue"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
