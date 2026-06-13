"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ApplicationType: TypeAlias = Literal[
    "HANA",
    "SAP_ABAP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HANA",
        "SAP_ABAP",
    )
)


def serialize_json(value: ApplicationType) -> str:
    return value


def deserialize_json(data: str) -> ApplicationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplicationType value: {data!r}")
    return cast(ApplicationType, data)
