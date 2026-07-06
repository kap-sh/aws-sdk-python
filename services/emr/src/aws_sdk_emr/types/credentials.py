"""Generated from Smithy shape ``com.amazonaws.emr#Credentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_emr.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_emr.types.username_password


class _Credentials_UsernamePassword(TypedDict, closed=True):
    UsernamePassword: "aws_sdk_emr.types.username_password.UsernamePassword"


Credentials: TypeAlias = _Credentials_UsernamePassword


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Credentials) -> dict:
    if "UsernamePassword" in value:
        import aws_sdk_emr.types.username_password

        return {
            "UsernamePassword": aws_sdk_emr.types.username_password.serialize_aws_json_1_1(
                value["UsernamePassword"]
            )
        }
    else:
        raise SerializationError("Credentials: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Credentials:
    if "UsernamePassword" in data:
        import aws_sdk_emr.types.username_password

        return {
            "UsernamePassword": aws_sdk_emr.types.username_password.deserialize_aws_json_1_1(
                data["UsernamePassword"]
            )
        }
    else:
        raise DeserializationError("Credentials: no recognized variant key")
