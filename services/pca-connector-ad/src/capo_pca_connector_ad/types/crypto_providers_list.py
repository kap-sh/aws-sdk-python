"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#CryptoProvidersList``."""

from typing import TypeAlias

CryptoProvidersList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: CryptoProvidersList) -> list:
    return list(value)


def deserialize_json(data: list) -> CryptoProvidersList:
    return list(data)
