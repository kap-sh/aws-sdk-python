"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionApiKeyAuthResponseParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.auth_header_parameters


class ConnectionApiKeyAuthResponseParameters(TypedDict, closed=True):
    api_key_name: NotRequired[
        "capo_eventbridge.types.auth_header_parameters.AuthHeaderParameters"
    ]
    """<p>The name of the header to use for the <code>APIKeyValue</code> used for authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionApiKeyAuthResponseParameters) -> dict:
    out: dict = {}
    if "api_key_name" in value:
        out["ApiKeyName"] = value["api_key_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionApiKeyAuthResponseParameters:
    out: ConnectionApiKeyAuthResponseParameters = {}  # type: ignore[typeddict-item]
    if data.get("ApiKeyName") is not None:
        out["api_key_name"] = data["ApiKeyName"]
    return out
