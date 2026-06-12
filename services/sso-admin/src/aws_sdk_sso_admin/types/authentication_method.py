"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AuthenticationMethod``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_sso_admin.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sso_admin.types.iam_authentication_method


class _AuthenticationMethod_Iam(TypedDict):
    Iam: "aws_sdk_sso_admin.types.iam_authentication_method.IamAuthenticationMethod"


AuthenticationMethod: TypeAlias = _AuthenticationMethod_Iam


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMethod) -> dict:
    if "Iam" in value:
        import aws_sdk_sso_admin.types.iam_authentication_method

        return {
            "Iam": aws_sdk_sso_admin.types.iam_authentication_method.serialize_aws_json_1_1(
                value["Iam"]
            )
        }
    else:
        raise SerializationError("AuthenticationMethod: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AuthenticationMethod:
    if "Iam" in data:
        import aws_sdk_sso_admin.types.iam_authentication_method

        return {
            "Iam": aws_sdk_sso_admin.types.iam_authentication_method.deserialize_aws_json_1_1(
                data["Iam"]
            )
        }
    else:
        raise DeserializationError("AuthenticationMethod: no recognized variant key")
