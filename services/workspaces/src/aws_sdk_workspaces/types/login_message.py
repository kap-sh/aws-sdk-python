"""Generated from Smithy shape ``com.amazonaws.workspaces#LoginMessage``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.client_locale
    import aws_sdk_workspaces.types.client_login_message

LoginMessage: TypeAlias = dict[
    "aws_sdk_workspaces.types.client_locale.ClientLocale",
    "aws_sdk_workspaces.types.client_login_message.ClientLoginMessage",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: LoginMessage) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> LoginMessage:
    out: LoginMessage = {}
    for key, value in data.items():
        out[key] = value
    return out
