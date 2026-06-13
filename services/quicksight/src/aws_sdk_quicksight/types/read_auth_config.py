"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.connection_auth_type
    import aws_sdk_quicksight.types.read_authentication_metadata


class ReadAuthConfig(TypedDict):
    authentication_type: (
        "aws_sdk_quicksight.types.connection_auth_type.ConnectionAuthType"
    )
    """<p>The type of authentication being used (BASIC, API_KEY, OAUTH2_CLIENT_CREDENTIALS, or OAUTH2_AUTHORIZATION_CODE).</p>"""
    authentication_metadata: "aws_sdk_quicksight.types.read_authentication_metadata.ReadAuthenticationMetadata"
    """<p>The authentication metadata containing configuration details specific to the authentication type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthConfig) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.connection_auth_type

    out["AuthenticationType"] = (
        aws_sdk_quicksight.types.connection_auth_type.serialize_json(
            value["authentication_type"]
        )
    )
    import aws_sdk_quicksight.types.read_authentication_metadata

    out["AuthenticationMetadata"] = (
        aws_sdk_quicksight.types.read_authentication_metadata.serialize_json(
            value["authentication_metadata"]
        )
    )
    return out


def deserialize_json(data: dict) -> ReadAuthConfig:
    out: ReadAuthConfig = {}  # type: ignore[typeddict-item]
    if "AuthenticationType" in data:
        import aws_sdk_quicksight.types.connection_auth_type

        out["authentication_type"] = (
            aws_sdk_quicksight.types.connection_auth_type.deserialize_json(
                data["AuthenticationType"]
            )
        )
    else:
        raise DeserializationError("ReadAuthConfig.authentication_type required")
    if "AuthenticationMetadata" in data:
        import aws_sdk_quicksight.types.read_authentication_metadata

        out["authentication_metadata"] = (
            aws_sdk_quicksight.types.read_authentication_metadata.deserialize_json(
                data["AuthenticationMetadata"]
            )
        )
    else:
        raise DeserializationError("ReadAuthConfig.authentication_metadata required")
    return out
