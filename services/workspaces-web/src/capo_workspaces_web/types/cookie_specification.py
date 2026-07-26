"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CookieSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.cookie_domain
    import capo_workspaces_web.types.cookie_name
    import capo_workspaces_web.types.cookie_path


class CookieSpecification(TypedDict, closed=True):
    domain: "capo_workspaces_web.types.cookie_domain.CookieDomain"
    """<p>The domain of the cookie.</p>"""
    name: NotRequired["capo_workspaces_web.types.cookie_name.CookieName"]
    """<p>The name of the cookie.</p>"""
    path: NotRequired["capo_workspaces_web.types.cookie_path.CookiePath"]
    """<p>The path of the cookie.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CookieSpecification) -> dict:
    out: dict = {}
    out["domain"] = value["domain"]
    if "name" in value:
        out["name"] = value["name"]
    if "path" in value:
        out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> CookieSpecification:
    out: CookieSpecification = {}  # type: ignore[typeddict-item]
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("CookieSpecification.domain required")
    if "name" in data:
        out["name"] = data["name"]
    if "path" in data:
        out["path"] = data["path"]
    return out
