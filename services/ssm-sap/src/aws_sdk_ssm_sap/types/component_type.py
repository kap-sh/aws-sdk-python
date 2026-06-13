"""Generated from Smithy shape ``com.amazonaws.ssmsap#ComponentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ComponentType: TypeAlias = Literal[
    "HANA",
    "HANA_NODE",
    "ABAP",
    "ASCS",
    "DIALOG",
    "WEBDISP",
    "WD",
    "ERS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HANA",
        "HANA_NODE",
        "ABAP",
        "ASCS",
        "DIALOG",
        "WEBDISP",
        "WD",
        "ERS",
    )
)


def serialize_json(value: ComponentType) -> str:
    return value


def deserialize_json(data: str) -> ComponentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComponentType value: {data!r}")
    return cast(ComponentType, data)
