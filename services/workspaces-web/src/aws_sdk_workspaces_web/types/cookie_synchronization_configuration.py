"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CookieSynchronizationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_workspaces_web.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.cookie_specifications

class CookieSynchronizationConfiguration(TypedDict):
    allowlist: "aws_sdk_workspaces_web.types.cookie_specifications.CookieSpecifications"
    """<p>The list of cookie specifications that are allowed to be synchronized to the remote browser.</p>"""
    blocklist: NotRequired["aws_sdk_workspaces_web.types.cookie_specifications.CookieSpecifications"]
    """<p>The list of cookie specifications that are blocked from being synchronized to the remote browser.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CookieSynchronizationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_workspaces_web.types.cookie_specifications
    out["allowlist"] = aws_sdk_workspaces_web.types.cookie_specifications.serialize_json(value["allowlist"])
    if "blocklist" in value:
        import aws_sdk_workspaces_web.types.cookie_specifications
        out["blocklist"] = aws_sdk_workspaces_web.types.cookie_specifications.serialize_json(value["blocklist"])
    return out


def deserialize_json(data: dict) -> CookieSynchronizationConfiguration:
    out: CookieSynchronizationConfiguration = {}  # type: ignore[typeddict-item]
    if "allowlist" in data:
        import aws_sdk_workspaces_web.types.cookie_specifications
        out["allowlist"] = aws_sdk_workspaces_web.types.cookie_specifications.deserialize_json(data["allowlist"])
    else:
        raise DeserializationError("CookieSynchronizationConfiguration.allowlist required")
    if "blocklist" in data:
        import aws_sdk_workspaces_web.types.cookie_specifications
        out["blocklist"] = aws_sdk_workspaces_web.types.cookie_specifications.deserialize_json(data["blocklist"])
    return out