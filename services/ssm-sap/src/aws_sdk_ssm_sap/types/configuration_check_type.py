"""Generated from Smithy shape ``com.amazonaws.ssmsap#ConfigurationCheckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm_sap.errors import DeserializationError

ConfigurationCheckType: TypeAlias = Literal[
    "SAP_CHECK_01",
    "SAP_CHECK_02",
    "SAP_CHECK_03",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAP_CHECK_01",
        "SAP_CHECK_02",
        "SAP_CHECK_03",
    )
)


def serialize_json(value: ConfigurationCheckType) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationCheckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationCheckType value: {data!r}")
    return cast(ConfigurationCheckType, data)
