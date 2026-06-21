"""Generated from Smithy shape ``com.amazonaws.amplifybackend#DeliveryMethod``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of verification message to send.</p>"""
DeliveryMethod: TypeAlias = Literal[
    "EMAIL",
    "SMS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeliveryMethod) -> str:
    return value


def deserialize_json(data: str) -> DeliveryMethod:
    return cast(DeliveryMethod, data)
