"""Generated from Smithy shape ``com.amazonaws.quicksight#WebProxyCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.db_username
    import capo_quicksight.types.password


class WebProxyCredentials(TypedDict, closed=True):
    web_proxy_username: "capo_quicksight.types.db_username.DbUsername"
    """<p>The username for authenticating with the web proxy server.</p>"""
    web_proxy_password: "capo_quicksight.types.password.Password"
    """<p>The password for authenticating with the web proxy server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WebProxyCredentials) -> dict:
    out: dict = {}
    out["WebProxyUsername"] = value["web_proxy_username"]
    out["WebProxyPassword"] = value["web_proxy_password"]
    return out


def deserialize_json(data: dict) -> WebProxyCredentials:
    out: WebProxyCredentials = {}  # type: ignore[typeddict-item]
    if "WebProxyUsername" in data:
        out["web_proxy_username"] = data["WebProxyUsername"]
    else:
        raise DeserializationError("WebProxyCredentials.web_proxy_username required")
    if "WebProxyPassword" in data:
        out["web_proxy_password"] = data["WebProxyPassword"]
    else:
        raise DeserializationError("WebProxyCredentials.web_proxy_password required")
    return out
