"""Generated from Smithy shape ``com.amazonaws.controlcatalog#GovernedProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.governed_provider

GovernedProviders: TypeAlias = list[
    "aws_sdk_controlcatalog.types.governed_provider.GovernedProvider"
]


# --- restJson1 ser/de ---
def serialize_json(value: GovernedProviders) -> list:
    return list(value)


def deserialize_json(data: list) -> GovernedProviders:
    return list(data)
