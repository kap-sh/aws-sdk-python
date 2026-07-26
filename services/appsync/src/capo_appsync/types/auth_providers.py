"""Generated from Smithy shape ``com.amazonaws.appsync#AuthProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.auth_provider

AuthProviders: TypeAlias = list["capo_appsync.types.auth_provider.AuthProvider"]


# --- restJson1 ser/de ---
def serialize_json(value: AuthProviders) -> list:
    import capo_appsync.types.auth_provider

    out: list = []
    for item in value:
        out.append(capo_appsync.types.auth_provider.serialize_json(item))
    return out


def deserialize_json(data: list) -> AuthProviders:
    import capo_appsync.types.auth_provider

    out: AuthProviders = []
    for item in data:
        out.append(capo_appsync.types.auth_provider.deserialize_json(item))
    return out
