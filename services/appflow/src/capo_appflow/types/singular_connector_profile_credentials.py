"""Generated from Smithy shape ``com.amazonaws.appflow#SingularConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_key


class SingularConnectorProfileCredentials(TypedDict, closed=True):
    api_key: "capo_appflow.types.api_key.ApiKey"
    """<p> A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SingularConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiKey"] = value["api_key"]
    return out


def deserialize_json(data: dict) -> SingularConnectorProfileCredentials:
    out: SingularConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "apiKey" in data:
        out["api_key"] = data["apiKey"]
    else:
        raise DeserializationError(
            "SingularConnectorProfileCredentials.api_key required"
        )
    return out
