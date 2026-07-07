"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateConnectionOAuthClientRequestParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.auth_header_parameters
    import aws_sdk_eventbridge.types.auth_header_parameters_sensitive


class CreateConnectionOAuthClientRequestParameters(TypedDict, closed=True):
    client_id: "aws_sdk_eventbridge.types.auth_header_parameters.AuthHeaderParameters"
    """<p>The client ID to use for OAuth authorization for the connection.</p>"""
    client_secret: "aws_sdk_eventbridge.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    """<p>The client secret associated with the client ID to use for OAuth authorization for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionOAuthClientRequestParameters) -> dict:
    out: dict = {}
    out["ClientID"] = value["client_id"]
    out["ClientSecret"] = value["client_secret"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> CreateConnectionOAuthClientRequestParameters:
    out: CreateConnectionOAuthClientRequestParameters = {}  # type: ignore[typeddict-item]
    if "ClientID" in data:
        out["client_id"] = data["ClientID"]
    else:
        raise DeserializationError(
            "CreateConnectionOAuthClientRequestParameters.client_id required"
        )
    if "ClientSecret" in data:
        out["client_secret"] = data["ClientSecret"]
    else:
        raise DeserializationError(
            "CreateConnectionOAuthClientRequestParameters.client_secret required"
        )
    return out
