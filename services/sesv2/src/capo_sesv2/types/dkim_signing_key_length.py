"""Generated from Smithy shape ``com.amazonaws.sesv2#DkimSigningKeyLength``."""

from typing import Literal, TypeAlias, cast

DkimSigningKeyLength: TypeAlias = Literal[
    "RSA_1024_BIT",
    "RSA_2048_BIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: DkimSigningKeyLength) -> str:
    return value


def deserialize_json(data: str) -> DkimSigningKeyLength:
    return cast(DkimSigningKeyLength, data)
