"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceFunctionCriticality``."""

from typing import Literal, TypeAlias, cast

ServiceFunctionCriticality: TypeAlias = Literal[
    "PRIMARY",
    "SUPPLEMENTAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceFunctionCriticality) -> str:
    return value


def deserialize_json(data: str) -> ServiceFunctionCriticality:
    return cast(ServiceFunctionCriticality, data)
