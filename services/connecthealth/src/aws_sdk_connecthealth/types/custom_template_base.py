"""Generated from Smithy shape ``com.amazonaws.connecthealth#CustomTemplateBase``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connecthealth.errors import DeserializationError

CustomTemplateBase: TypeAlias = Literal[
    "HISTORY_AND_PHYSICAL",
    "GIRPP",
    "DAP",
    "SIRP",
    "BIRP",
    "BEHAVIORAL_SOAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HISTORY_AND_PHYSICAL",
        "GIRPP",
        "DAP",
        "SIRP",
        "BIRP",
        "BEHAVIORAL_SOAP",
    )
)


def serialize_json(value: CustomTemplateBase) -> str:
    return value


def deserialize_json(data: str) -> CustomTemplateBase:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomTemplateBase value: {data!r}")
    return cast(CustomTemplateBase, data)
