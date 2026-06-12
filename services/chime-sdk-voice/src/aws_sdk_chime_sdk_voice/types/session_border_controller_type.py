"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#SessionBorderControllerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

SessionBorderControllerType: TypeAlias = Literal[
    "RIBBON_SBC",
    "ORACLE_ACME_PACKET_SBC",
    "AVAYA_SBCE",
    "CISCO_UNIFIED_BORDER_ELEMENT",
    "AUDIOCODES_MEDIANT_SBC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RIBBON_SBC",
        "ORACLE_ACME_PACKET_SBC",
        "AVAYA_SBCE",
        "CISCO_UNIFIED_BORDER_ELEMENT",
        "AUDIOCODES_MEDIANT_SBC",
    )
)


def serialize_json(value: SessionBorderControllerType) -> str:
    return value


def deserialize_json(data: str) -> SessionBorderControllerType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SessionBorderControllerType value: {data!r}"
        )
    return cast(SessionBorderControllerType, data)
