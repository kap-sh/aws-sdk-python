"""Generated from Smithy shape ``com.amazonaws.appsync#AuthProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appsync.types.auth_provider

AuthProviders: TypeAlias = list["aws_sdk_appsync.types.auth_provider.AuthProvider"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthProviders) -> list:
    import aws_sdk_appsync.types.auth_provider

    out: list = []
    for item in value:
        out.append(aws_sdk_appsync.types.auth_provider.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthProviders:
    import aws_sdk_appsync.types.auth_provider

    out: AuthProviders = []
    for item in data:
        out.append(aws_sdk_appsync.types.auth_provider.deserialize_json(item))
    return out
