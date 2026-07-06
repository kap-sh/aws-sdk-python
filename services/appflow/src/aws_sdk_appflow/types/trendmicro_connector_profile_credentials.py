"""Generated from Smithy shape ``com.amazonaws.appflow#TrendmicroConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.api_secret_key


class TrendmicroConnectorProfileCredentials(TypedDict, closed=True):
    api_secret_key: "aws_sdk_appflow.types.api_secret_key.ApiSecretKey"
    """<p> The Secret Access Key portion of the credentials. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrendmicroConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["apiSecretKey"] = value["api_secret_key"]
    return out


def deserialize_json(data: dict) -> TrendmicroConnectorProfileCredentials:
    out: TrendmicroConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "apiSecretKey" in data:
        out["api_secret_key"] = data["apiSecretKey"]
    else:
        raise DeserializationError(
            "TrendmicroConnectorProfileCredentials.api_secret_key required"
        )
    return out
