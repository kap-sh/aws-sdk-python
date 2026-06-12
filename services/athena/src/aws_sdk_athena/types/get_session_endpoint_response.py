"""Generated from Smithy shape ``com.amazonaws.athena#GetSessionEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.string
    import aws_sdk_athena.types.timestamp


class GetSessionEndpointResponse(TypedDict):
    endpoint_url: "aws_sdk_athena.types.string.String"
    """<p>The endpoint for connecting to the session.</p>"""
    auth_token: "aws_sdk_athena.types.string.String"
    """<p>Authentication token for the connection</p>"""
    auth_token_expiration_time: "aws_sdk_athena.types.timestamp.Timestamp"
    """<p>Expiration time of the auth token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSessionEndpointResponse) -> dict:
    out: dict = {}
    out["EndpointUrl"] = value["endpoint_url"]
    out["AuthToken"] = value["auth_token"]
    import aws_sdk_athena.types.timestamp

    out["AuthTokenExpirationTime"] = (
        aws_sdk_athena.types.timestamp.serialize_aws_json_1_1(
            value["auth_token_expiration_time"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSessionEndpointResponse:
    out: GetSessionEndpointResponse = {}  # type: ignore[typeddict-item]
    if "EndpointUrl" in data:
        out["endpoint_url"] = data["EndpointUrl"]
    else:
        raise DeserializationError("GetSessionEndpointResponse.endpoint_url required")
    if "AuthToken" in data:
        out["auth_token"] = data["AuthToken"]
    else:
        raise DeserializationError("GetSessionEndpointResponse.auth_token required")
    if "AuthTokenExpirationTime" in data:
        import aws_sdk_athena.types.timestamp

        out["auth_token_expiration_time"] = (
            aws_sdk_athena.types.timestamp.deserialize_aws_json_1_1(
                data["AuthTokenExpirationTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetSessionEndpointResponse.auth_token_expiration_time required"
        )
    return out
