"""Generated from Smithy shape ``com.amazonaws.appsync#AdditionalAuthenticationProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appsync.types.additional_authentication_provider

AdditionalAuthenticationProviders: TypeAlias = list[
    "capo_appsync.types.additional_authentication_provider.AdditionalAuthenticationProvider"
]


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalAuthenticationProviders) -> list:
    import capo_appsync.types.additional_authentication_provider

    out: list = []
    for item in value:
        out.append(
            capo_appsync.types.additional_authentication_provider.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AdditionalAuthenticationProviders:
    import capo_appsync.types.additional_authentication_provider

    out: AdditionalAuthenticationProviders = []
    for item in data:
        out.append(
            capo_appsync.types.additional_authentication_provider.deserialize_json(item)
        )
    return out
