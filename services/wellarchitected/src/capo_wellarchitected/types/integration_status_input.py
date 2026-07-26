"""Generated from Smithy shape ``com.amazonaws.wellarchitected#IntegrationStatusInput``."""

from typing import Literal, TypeAlias, cast

IntegrationStatusInput: TypeAlias = Literal["NOT_CONFIGURED",]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationStatusInput) -> str:
    return value


def deserialize_json(data: str) -> IntegrationStatusInput:
    return cast(IntegrationStatusInput, data)
