"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ServerEndpoint``."""

from typing_extensions import NotRequired, TypedDict


class ServerEndpoint(TypedDict, closed=True):
    endpoint: NotRequired["str"]
    """<p>The network address of the endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerEndpoint) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    return out


def deserialize_json(data: dict) -> ServerEndpoint:
    out: ServerEndpoint = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    return out
