"""Generated from Smithy shape ``com.amazonaws.quicksight#BasicAuthConnectionMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.action_password
    import capo_quicksight.types.action_user_name
    import capo_quicksight.types.endpoint


class BasicAuthConnectionMetadata(TypedDict, closed=True):
    base_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The base URL endpoint for the external service.</p>"""
    username: "capo_quicksight.types.action_user_name.ActionUserName"
    """<p>The username for basic authentication.</p>"""
    password: "capo_quicksight.types.action_password.ActionPassword"
    """<p>The password for basic authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicAuthConnectionMetadata) -> dict:
    out: dict = {}
    out["BaseEndpoint"] = value["base_endpoint"]
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_json(data: dict) -> BasicAuthConnectionMetadata:
    out: BasicAuthConnectionMetadata = {}  # type: ignore[typeddict-item]
    if "BaseEndpoint" in data:
        out["base_endpoint"] = data["BaseEndpoint"]
    else:
        raise DeserializationError("BasicAuthConnectionMetadata.base_endpoint required")
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("BasicAuthConnectionMetadata.username required")
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("BasicAuthConnectionMetadata.password required")
    return out
