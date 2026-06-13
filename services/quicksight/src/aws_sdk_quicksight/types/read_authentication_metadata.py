"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthenticationMetadata``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.read_api_key_connection_metadata
    import aws_sdk_quicksight.types.read_authorization_code_grant_metadata
    import aws_sdk_quicksight.types.read_basic_auth_connection_metadata
    import aws_sdk_quicksight.types.read_client_credentials_grant_metadata
    import aws_sdk_quicksight.types.read_iam_connection_metadata
    import aws_sdk_quicksight.types.read_none_connection_metadata


class _ReadAuthenticationMetadata_AuthorizationCodeGrantMetadata(TypedDict):
    AuthorizationCodeGrantMetadata: "aws_sdk_quicksight.types.read_authorization_code_grant_metadata.ReadAuthorizationCodeGrantMetadata"


class _ReadAuthenticationMetadata_ClientCredentialsGrantMetadata(TypedDict):
    ClientCredentialsGrantMetadata: "aws_sdk_quicksight.types.read_client_credentials_grant_metadata.ReadClientCredentialsGrantMetadata"


class _ReadAuthenticationMetadata_BasicAuthConnectionMetadata(TypedDict):
    BasicAuthConnectionMetadata: "aws_sdk_quicksight.types.read_basic_auth_connection_metadata.ReadBasicAuthConnectionMetadata"


class _ReadAuthenticationMetadata_ApiKeyConnectionMetadata(TypedDict):
    ApiKeyConnectionMetadata: "aws_sdk_quicksight.types.read_api_key_connection_metadata.ReadAPIKeyConnectionMetadata"


class _ReadAuthenticationMetadata_NoneConnectionMetadata(TypedDict):
    NoneConnectionMetadata: "aws_sdk_quicksight.types.read_none_connection_metadata.ReadNoneConnectionMetadata"


class _ReadAuthenticationMetadata_IamConnectionMetadata(TypedDict):
    IamConnectionMetadata: "aws_sdk_quicksight.types.read_iam_connection_metadata.ReadIamConnectionMetadata"


ReadAuthenticationMetadata: TypeAlias = (
    _ReadAuthenticationMetadata_AuthorizationCodeGrantMetadata
    | _ReadAuthenticationMetadata_ClientCredentialsGrantMetadata
    | _ReadAuthenticationMetadata_BasicAuthConnectionMetadata
    | _ReadAuthenticationMetadata_ApiKeyConnectionMetadata
    | _ReadAuthenticationMetadata_NoneConnectionMetadata
    | _ReadAuthenticationMetadata_IamConnectionMetadata
)


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthenticationMetadata) -> dict:
    if "AuthorizationCodeGrantMetadata" in value:
        import aws_sdk_quicksight.types.read_authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": aws_sdk_quicksight.types.read_authorization_code_grant_metadata.serialize_json(
                value["AuthorizationCodeGrantMetadata"]
            )
        }
    elif "ClientCredentialsGrantMetadata" in value:
        import aws_sdk_quicksight.types.read_client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": aws_sdk_quicksight.types.read_client_credentials_grant_metadata.serialize_json(
                value["ClientCredentialsGrantMetadata"]
            )
        }
    elif "BasicAuthConnectionMetadata" in value:
        import aws_sdk_quicksight.types.read_basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": aws_sdk_quicksight.types.read_basic_auth_connection_metadata.serialize_json(
                value["BasicAuthConnectionMetadata"]
            )
        }
    elif "ApiKeyConnectionMetadata" in value:
        import aws_sdk_quicksight.types.read_api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": aws_sdk_quicksight.types.read_api_key_connection_metadata.serialize_json(
                value["ApiKeyConnectionMetadata"]
            )
        }
    elif "NoneConnectionMetadata" in value:
        import aws_sdk_quicksight.types.read_none_connection_metadata

        return {
            "NoneConnectionMetadata": aws_sdk_quicksight.types.read_none_connection_metadata.serialize_json(
                value["NoneConnectionMetadata"]
            )
        }
    elif "IamConnectionMetadata" in value:
        import aws_sdk_quicksight.types.read_iam_connection_metadata

        return {
            "IamConnectionMetadata": aws_sdk_quicksight.types.read_iam_connection_metadata.serialize_json(
                value["IamConnectionMetadata"]
            )
        }
    else:
        raise SerializationError("ReadAuthenticationMetadata: no variant present")


def deserialize_json(data: dict) -> ReadAuthenticationMetadata:
    if "AuthorizationCodeGrantMetadata" in data:
        import aws_sdk_quicksight.types.read_authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": aws_sdk_quicksight.types.read_authorization_code_grant_metadata.deserialize_json(
                data["AuthorizationCodeGrantMetadata"]
            )
        }
    elif "ClientCredentialsGrantMetadata" in data:
        import aws_sdk_quicksight.types.read_client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": aws_sdk_quicksight.types.read_client_credentials_grant_metadata.deserialize_json(
                data["ClientCredentialsGrantMetadata"]
            )
        }
    elif "BasicAuthConnectionMetadata" in data:
        import aws_sdk_quicksight.types.read_basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": aws_sdk_quicksight.types.read_basic_auth_connection_metadata.deserialize_json(
                data["BasicAuthConnectionMetadata"]
            )
        }
    elif "ApiKeyConnectionMetadata" in data:
        import aws_sdk_quicksight.types.read_api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": aws_sdk_quicksight.types.read_api_key_connection_metadata.deserialize_json(
                data["ApiKeyConnectionMetadata"]
            )
        }
    elif "NoneConnectionMetadata" in data:
        import aws_sdk_quicksight.types.read_none_connection_metadata

        return {
            "NoneConnectionMetadata": aws_sdk_quicksight.types.read_none_connection_metadata.deserialize_json(
                data["NoneConnectionMetadata"]
            )
        }
    elif "IamConnectionMetadata" in data:
        import aws_sdk_quicksight.types.read_iam_connection_metadata

        return {
            "IamConnectionMetadata": aws_sdk_quicksight.types.read_iam_connection_metadata.deserialize_json(
                data["IamConnectionMetadata"]
            )
        }
    else:
        raise DeserializationError(
            "ReadAuthenticationMetadata: no recognized variant key"
        )
