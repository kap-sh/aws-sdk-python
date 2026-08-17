"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProvidersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.capacity_provider

CapacityProvidersList: TypeAlias = list[
    "capo_lambda.types.capacity_provider.CapacityProvider"
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProvidersList) -> list:
    import capo_lambda.types.capacity_provider

    out: list = []
    for item in value:
        out.append(capo_lambda.types.capacity_provider.serialize_json(item))
    return out


def deserialize_json(data: list) -> CapacityProvidersList:
    import capo_lambda.types.capacity_provider

    out: CapacityProvidersList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.capacity_provider.deserialize_json(item))
    return out
