"""Generated from Smithy shape ``com.amazonaws.appflow#DynatraceConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.api_token


class DynatraceConnectorProfileCredentials(TypedDict, closed=True):
    api_token: "capo_appflow.types.api_token.ApiToken"
    """<p> The API tokens used by Dynatrace API to authenticate various API calls. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiToken"] = value["api_token"]
    return out


def deserialize_json(data: dict) -> DynatraceConnectorProfileCredentials:
    out: DynatraceConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "apiToken" in data:
        out["api_token"] = data["apiToken"]
    else:
        raise DeserializationError(
            "DynatraceConnectorProfileCredentials.api_token required"
        )
    return out
