"""Generated from Smithy shape ``com.amazonaws.iot#TlsContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.server_name


class TlsContext(TypedDict, closed=True):
    server_name: NotRequired["aws_sdk_iot.types.server_name.ServerName"]
    """<p>The value of the <code>serverName</code> key in a TLS authorization request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsContext) -> dict:
    out: dict = {}
    if "server_name" in value:
        out["serverName"] = value["server_name"]
    return out


def deserialize_json(data: dict) -> TlsContext:
    out: TlsContext = {}  # type: ignore[typeddict-item]
    if "serverName" in data:
        out["server_name"] = data["serverName"]
    return out
