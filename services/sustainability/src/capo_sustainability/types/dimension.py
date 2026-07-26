"""Generated from Smithy shape ``com.amazonaws.sustainability#Dimension``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies the dimensions available for grouping and filtering emissions data.</p>"""
Dimension: TypeAlias = Literal[
    "USAGE_ACCOUNT_ID",
    "REGION",
    "SERVICE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Dimension) -> str:
    return value


def deserialize_json(data: str) -> Dimension:
    return cast(Dimension, data)
