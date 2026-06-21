"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#PaymentHttpMethodType``."""

from typing import Literal, TypeAlias, cast

PaymentHttpMethodType: TypeAlias = Literal[
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentHttpMethodType) -> str:
    return value


def deserialize_json(data: str) -> PaymentHttpMethodType:
    return cast(PaymentHttpMethodType, data)
