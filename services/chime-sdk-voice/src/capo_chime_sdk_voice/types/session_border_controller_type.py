"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SessionBorderControllerType``."""

from typing import Literal, TypeAlias, cast

SessionBorderControllerType: TypeAlias = Literal[
    "RIBBON_SBC",
    "ORACLE_ACME_PACKET_SBC",
    "AVAYA_SBCE",
    "CISCO_UNIFIED_BORDER_ELEMENT",
    "AUDIOCODES_MEDIANT_SBC",
]


# --- restJson1 ser/de ---
def serialize_json(value: SessionBorderControllerType) -> str:
    return value


def deserialize_json(data: str) -> SessionBorderControllerType:
    return cast(SessionBorderControllerType, data)
