"""Generated from Smithy shape ``com.amazonaws.mailmanager#RelayAuthentication``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.no_authentication
    import aws_sdk_mailmanager.types.secret_arn


class _RelayAuthentication_SecretArn(TypedDict, closed=True):
    SecretArn: "aws_sdk_mailmanager.types.secret_arn.SecretArn"


class _RelayAuthentication_NoAuthentication(TypedDict, closed=True):
    NoAuthentication: "aws_sdk_mailmanager.types.no_authentication.NoAuthentication"


RelayAuthentication: TypeAlias = (
    _RelayAuthentication_SecretArn | _RelayAuthentication_NoAuthentication
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelayAuthentication) -> dict:
    if "SecretArn" in value:
        return {"SecretArn": value["SecretArn"]}
    elif "NoAuthentication" in value:
        import aws_sdk_mailmanager.types.no_authentication

        return {
            "NoAuthentication": aws_sdk_mailmanager.types.no_authentication.serialize_aws_json_1_0(
                value["NoAuthentication"]
            )
        }
    else:
        raise SerializationError("RelayAuthentication: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RelayAuthentication:
    if "SecretArn" in data:
        return {"SecretArn": data["SecretArn"]}
    elif "NoAuthentication" in data:
        import aws_sdk_mailmanager.types.no_authentication

        return {
            "NoAuthentication": aws_sdk_mailmanager.types.no_authentication.deserialize_aws_json_1_0(
                data["NoAuthentication"]
            )
        }
    else:
        raise DeserializationError("RelayAuthentication: no recognized variant key")
