"""Generated from Smithy shape ``com.amazonaws.iotwireless#SigningAlg``."""

from typing import Literal, TypeAlias, cast

"""<p>The certificate chain algorithm provided by sidewalk.</p>"""
SigningAlg: TypeAlias = Literal[
    "Ed25519",
    "P256r1",
]


# --- restJson1 ser/de ---
def serialize_json(value: SigningAlg) -> str:
    return value


def deserialize_json(data: str) -> SigningAlg:
    return cast(SigningAlg, data)
