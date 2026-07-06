"""Generated from Smithy shape ``com.amazonaws.eventbridge#UpdateConnectionApiKeyAuthRequestParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.auth_header_parameters
    import aws_sdk_eventbridge.types.auth_header_parameters_sensitive


class UpdateConnectionApiKeyAuthRequestParameters(TypedDict, closed=True):
    api_key_name: NotRequired[
        "aws_sdk_eventbridge.types.auth_header_parameters.AuthHeaderParameters"
    ]
    """<p>The name of the API key to use for authorization.</p>"""
    api_key_value: NotRequired[
        "aws_sdk_eventbridge.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    ]
    """<p>The value associated with the API key to use for authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionApiKeyAuthRequestParameters) -> dict:
    out: dict = {}
    if "api_key_name" in value:
        out["ApiKeyName"] = value["api_key_name"]
    if "api_key_value" in value:
        out["ApiKeyValue"] = value["api_key_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionApiKeyAuthRequestParameters:
    out: UpdateConnectionApiKeyAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if "ApiKeyName" in data:
        out["api_key_name"] = data["ApiKeyName"]
    if "ApiKeyValue" in data:
        out["api_key_value"] = data["ApiKeyValue"]
    return out
