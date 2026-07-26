"""Generated from Smithy shape ``com.amazonaws.grafana#AuthenticationProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_grafana.types.authentication_provider_types

AuthenticationProviders: TypeAlias = list[
    "capo_grafana.types.authentication_provider_types.AuthenticationProviderTypes"
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationProviders) -> list:
    return list(value)


def deserialize_json(data: list) -> AuthenticationProviders:
    return list(data)
