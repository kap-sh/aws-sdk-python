"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccount``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.linked_account_developer_jwt
    import aws_sdk_bedrock_agentcore.types.linked_account_email
    import aws_sdk_bedrock_agentcore.types.linked_account_o_auth2
    import aws_sdk_bedrock_agentcore.types.linked_account_sms


class _LinkedAccount_email(TypedDict):
    email: "aws_sdk_bedrock_agentcore.types.linked_account_email.LinkedAccountEmail"


class _LinkedAccount_sms(TypedDict):
    sms: "aws_sdk_bedrock_agentcore.types.linked_account_sms.LinkedAccountSms"


class _LinkedAccount_developerJwt(TypedDict):
    developerJwt: "aws_sdk_bedrock_agentcore.types.linked_account_developer_jwt.LinkedAccountDeveloperJwt"


class _LinkedAccount_oAuth2(TypedDict):
    oAuth2: "aws_sdk_bedrock_agentcore.types.linked_account_o_auth2.LinkedAccountOAuth2"


LinkedAccount: TypeAlias = (
    _LinkedAccount_email
    | _LinkedAccount_sms
    | _LinkedAccount_developerJwt
    | _LinkedAccount_oAuth2
)


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccount) -> dict:
    if "email" in value:
        import aws_sdk_bedrock_agentcore.types.linked_account_email

        return {
            "email": aws_sdk_bedrock_agentcore.types.linked_account_email.serialize_json(
                value["email"]
            )
        }
    elif "sms" in value:
        import aws_sdk_bedrock_agentcore.types.linked_account_sms

        return {
            "sms": aws_sdk_bedrock_agentcore.types.linked_account_sms.serialize_json(
                value["sms"]
            )
        }
    elif "developerJwt" in value:
        import aws_sdk_bedrock_agentcore.types.linked_account_developer_jwt

        return {
            "developerJwt": aws_sdk_bedrock_agentcore.types.linked_account_developer_jwt.serialize_json(
                value["developerJwt"]
            )
        }
    elif "oAuth2" in value:
        import aws_sdk_bedrock_agentcore.types.linked_account_o_auth2

        return {
            "oAuth2": aws_sdk_bedrock_agentcore.types.linked_account_o_auth2.serialize_json(
                value["oAuth2"]
            )
        }
    else:
        raise SerializationError("LinkedAccount: no variant present")


def deserialize_json(data: dict) -> LinkedAccount:
    if "email" in data:
        import aws_sdk_bedrock_agentcore.types.linked_account_email

        return {
            "email": aws_sdk_bedrock_agentcore.types.linked_account_email.deserialize_json(
                data["email"]
            )
        }
    elif "sms" in data:
        import aws_sdk_bedrock_agentcore.types.linked_account_sms

        return {
            "sms": aws_sdk_bedrock_agentcore.types.linked_account_sms.deserialize_json(
                data["sms"]
            )
        }
    elif "developerJwt" in data:
        import aws_sdk_bedrock_agentcore.types.linked_account_developer_jwt

        return {
            "developerJwt": aws_sdk_bedrock_agentcore.types.linked_account_developer_jwt.deserialize_json(
                data["developerJwt"]
            )
        }
    elif "oAuth2" in data:
        import aws_sdk_bedrock_agentcore.types.linked_account_o_auth2

        return {
            "oAuth2": aws_sdk_bedrock_agentcore.types.linked_account_o_auth2.deserialize_json(
                data["oAuth2"]
            )
        }
    else:
        raise DeserializationError("LinkedAccount: no recognized variant key")
