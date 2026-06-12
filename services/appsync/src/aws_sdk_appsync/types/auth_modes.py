"""Generated from Smithy shape ``com.amazonaws.appsync#AuthModes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.auth_mode

AuthModes: TypeAlias = list["aws_sdk_appsync.types.auth_mode.AuthMode"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthModes) -> list:
    import aws_sdk_appsync.types.auth_mode

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.auth_mode.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthModes:
    import aws_sdk_appsync.types.auth_mode

    out: AuthModes = []
    for item in data:
        out.append(aws_sdk_appsync.types.auth_mode.deserialize_json(item))
    return out
