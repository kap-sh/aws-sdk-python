"""Generated from Smithy shape ``com.amazonaws.iotwireless#DlClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

"""<p>DlClass for LoRaWAM, valid values are ClassB and ClassC.</p>"""
DlClass: TypeAlias = Literal[
    "ClassB",
    "ClassC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ClassB",
        "ClassC",
    )
)


def serialize_json(value: DlClass) -> str:
    return value


def deserialize_json(data: str) -> DlClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DlClass value: {data!r}")
    return cast(DlClass, data)
