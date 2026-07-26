"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#RandomKeyMaxLength``."""

from typing import Literal, TypeAlias, cast

RandomKeyMaxLength: TypeAlias = Literal[
    "BYTES_8",
    "BYTES_16",
    "BYTES_24",
]


# --- restJson1 ser/de ---
def serialize_json(value: RandomKeyMaxLength) -> str:
    return value


def deserialize_json(data: str) -> RandomKeyMaxLength:
    return cast(RandomKeyMaxLength, data)
