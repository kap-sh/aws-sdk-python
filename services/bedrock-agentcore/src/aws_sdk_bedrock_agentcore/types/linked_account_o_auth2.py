"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountOAuth2``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.o_auth2_authentication


class _LinkedAccountOAuth2_google(TypedDict, closed=True):
    google: (
        "aws_sdk_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"
    )


class _LinkedAccountOAuth2_apple(TypedDict, closed=True):
    apple: "aws_sdk_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"


class _LinkedAccountOAuth2_x(TypedDict, closed=True):
    x: "aws_sdk_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"


class _LinkedAccountOAuth2_telegram(TypedDict, closed=True):
    telegram: (
        "aws_sdk_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"
    )


class _LinkedAccountOAuth2_github(TypedDict, closed=True):
    github: (
        "aws_sdk_bedrock_agentcore.types.o_auth2_authentication.OAuth2Authentication"
    )


LinkedAccountOAuth2: TypeAlias = (
    _LinkedAccountOAuth2_google
    | _LinkedAccountOAuth2_apple
    | _LinkedAccountOAuth2_x
    | _LinkedAccountOAuth2_telegram
    | _LinkedAccountOAuth2_github
)


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountOAuth2) -> dict:
    if "google" in value:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "google": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["google"]
            )
        }
    elif "apple" in value:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "apple": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["apple"]
            )
        }
    elif "x" in value:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "x": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["x"]
            )
        }
    elif "telegram" in value:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "telegram": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["telegram"]
            )
        }
    elif "github" in value:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "github": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.serialize_json(
                value["github"]
            )
        }
    else:
        raise SerializationError("LinkedAccountOAuth2: no variant present")


def deserialize_json(data: dict) -> LinkedAccountOAuth2:
    if "google" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "google": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["google"]
            )
        }
    elif "apple" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "apple": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["apple"]
            )
        }
    elif "x" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "x": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["x"]
            )
        }
    elif "telegram" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "telegram": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["telegram"]
            )
        }
    elif "github" in data:
        import aws_sdk_bedrock_agentcore.types.o_auth2_authentication

        return {
            "github": aws_sdk_bedrock_agentcore.types.o_auth2_authentication.deserialize_json(
                data["github"]
            )
        }
    else:
        raise DeserializationError("LinkedAccountOAuth2: no recognized variant key")
