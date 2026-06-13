"""Generated from Smithy shape ``com.amazonaws.securityagent#HttpVerification``."""

from typing import TypedDict

from typing_extensions import NotRequired


class HttpVerification(TypedDict):
    token: NotRequired["str"]
    """<p>The verification token to serve at the specified route path.</p>"""
    route_path: NotRequired["str"]
    """<p>The HTTP route path where the verification token must be served.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpVerification) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    if "route_path" in value:
        out["routePath"] = value["route_path"]
    return out


def deserialize_json(data: dict) -> HttpVerification:
    out: HttpVerification = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    if "routePath" in data:
        out["route_path"] = data["routePath"]
    return out
