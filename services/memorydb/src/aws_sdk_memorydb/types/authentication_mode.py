"""Generated from Smithy shape ``com.amazonaws.memorydb#AuthenticationMode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.input_authentication_type
    import aws_sdk_memorydb.types.password_list_input


class AuthenticationMode(TypedDict):
    type: NotRequired[
        "aws_sdk_memorydb.types.input_authentication_type.InputAuthenticationType"
    ]
    """<p>Indicates whether the user requires a password to authenticate. All newly-created users require a password.</p>"""
    passwords: NotRequired[
        "aws_sdk_memorydb.types.password_list_input.PasswordListInput"
    ]
    """<p>The password(s) used for authentication</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationMode) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_memorydb.types.input_authentication_type

        out["Type"] = (
            aws_sdk_memorydb.types.input_authentication_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "passwords" in value:
        import aws_sdk_memorydb.types.password_list_input

        out["Passwords"] = (
            aws_sdk_memorydb.types.password_list_input.serialize_aws_json_1_1(
                value["passwords"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationMode:
    out: AuthenticationMode = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_memorydb.types.input_authentication_type

        out["type"] = (
            aws_sdk_memorydb.types.input_authentication_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "Passwords" in data:
        import aws_sdk_memorydb.types.password_list_input

        out["passwords"] = (
            aws_sdk_memorydb.types.password_list_input.deserialize_aws_json_1_1(
                data["Passwords"]
            )
        )
    return out
