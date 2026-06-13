"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthenticationMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.api_key_connection_metadata
    import aws_sdk_quicksight.types.authorization_code_grant_metadata
    import aws_sdk_quicksight.types.basic_auth_connection_metadata
    import aws_sdk_quicksight.types.client_credentials_grant_metadata
    import aws_sdk_quicksight.types.iam_connection_metadata
    import aws_sdk_quicksight.types.none_connection_metadata


class _AuthenticationMetadata_AuthorizationCodeGrantMetadata(TypedDict):
    AuthorizationCodeGrantMetadata: "aws_sdk_quicksight.types.authorization_code_grant_metadata.AuthorizationCodeGrantMetadata"


class _AuthenticationMetadata_ClientCredentialsGrantMetadata(TypedDict):
    ClientCredentialsGrantMetadata: "aws_sdk_quicksight.types.client_credentials_grant_metadata.ClientCredentialsGrantMetadata"


class _AuthenticationMetadata_BasicAuthConnectionMetadata(TypedDict):
    BasicAuthConnectionMetadata: "aws_sdk_quicksight.types.basic_auth_connection_metadata.BasicAuthConnectionMetadata"


class _AuthenticationMetadata_ApiKeyConnectionMetadata(TypedDict):
    ApiKeyConnectionMetadata: (
        "aws_sdk_quicksight.types.api_key_connection_metadata.APIKeyConnectionMetadata"
    )


class _AuthenticationMetadata_NoneConnectionMetadata(TypedDict):
    NoneConnectionMetadata: (
        "aws_sdk_quicksight.types.none_connection_metadata.NoneConnectionMetadata"
    )


class _AuthenticationMetadata_IamConnectionMetadata(TypedDict):
    IamConnectionMetadata: (
        "aws_sdk_quicksight.types.iam_connection_metadata.IAMConnectionMetadata"
    )


AuthenticationMetadata: TypeAlias = (
    _AuthenticationMetadata_AuthorizationCodeGrantMetadata
    | _AuthenticationMetadata_ClientCredentialsGrantMetadata
    | _AuthenticationMetadata_BasicAuthConnectionMetadata
    | _AuthenticationMetadata_ApiKeyConnectionMetadata
    | _AuthenticationMetadata_NoneConnectionMetadata
    | _AuthenticationMetadata_IamConnectionMetadata
)


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationMetadata) -> dict:
    if "AuthorizationCodeGrantMetadata" in value:
        import aws_sdk_quicksight.types.authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": aws_sdk_quicksight.types.authorization_code_grant_metadata.serialize_json(
                value["AuthorizationCodeGrantMetadata"]
            )
        }
    elif "ClientCredentialsGrantMetadata" in value:
        import aws_sdk_quicksight.types.client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": aws_sdk_quicksight.types.client_credentials_grant_metadata.serialize_json(
                value["ClientCredentialsGrantMetadata"]
            )
        }
    elif "BasicAuthConnectionMetadata" in value:
        import aws_sdk_quicksight.types.basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": aws_sdk_quicksight.types.basic_auth_connection_metadata.serialize_json(
                value["BasicAuthConnectionMetadata"]
            )
        }
    elif "ApiKeyConnectionMetadata" in value:
        import aws_sdk_quicksight.types.api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": aws_sdk_quicksight.types.api_key_connection_metadata.serialize_json(
                value["ApiKeyConnectionMetadata"]
            )
        }
    elif "NoneConnectionMetadata" in value:
        import aws_sdk_quicksight.types.none_connection_metadata

        return {
            "NoneConnectionMetadata": aws_sdk_quicksight.types.none_connection_metadata.serialize_json(
                value["NoneConnectionMetadata"]
            )
        }
    elif "IamConnectionMetadata" in value:
        import aws_sdk_quicksight.types.iam_connection_metadata

        return {
            "IamConnectionMetadata": aws_sdk_quicksight.types.iam_connection_metadata.serialize_json(
                value["IamConnectionMetadata"]
            )
        }
    else:
        raise SerializationError("AuthenticationMetadata: no variant present")


def deserialize_json(data: dict) -> AuthenticationMetadata:
    if "AuthorizationCodeGrantMetadata" in data:
        import aws_sdk_quicksight.types.authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": aws_sdk_quicksight.types.authorization_code_grant_metadata.deserialize_json(
                data["AuthorizationCodeGrantMetadata"]
            )
        }
    elif "ClientCredentialsGrantMetadata" in data:
        import aws_sdk_quicksight.types.client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": aws_sdk_quicksight.types.client_credentials_grant_metadata.deserialize_json(
                data["ClientCredentialsGrantMetadata"]
            )
        }
    elif "BasicAuthConnectionMetadata" in data:
        import aws_sdk_quicksight.types.basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": aws_sdk_quicksight.types.basic_auth_connection_metadata.deserialize_json(
                data["BasicAuthConnectionMetadata"]
            )
        }
    elif "ApiKeyConnectionMetadata" in data:
        import aws_sdk_quicksight.types.api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": aws_sdk_quicksight.types.api_key_connection_metadata.deserialize_json(
                data["ApiKeyConnectionMetadata"]
            )
        }
    elif "NoneConnectionMetadata" in data:
        import aws_sdk_quicksight.types.none_connection_metadata

        return {
            "NoneConnectionMetadata": aws_sdk_quicksight.types.none_connection_metadata.deserialize_json(
                data["NoneConnectionMetadata"]
            )
        }
    elif "IamConnectionMetadata" in data:
        import aws_sdk_quicksight.types.iam_connection_metadata

        return {
            "IamConnectionMetadata": aws_sdk_quicksight.types.iam_connection_metadata.deserialize_json(
                data["IamConnectionMetadata"]
            )
        }
    else:
        raise DeserializationError("AuthenticationMetadata: no recognized variant key")
