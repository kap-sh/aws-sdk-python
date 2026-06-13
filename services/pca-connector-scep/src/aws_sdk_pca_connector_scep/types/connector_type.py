"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_scep.errors import DeserializationError

ConnectorType: TypeAlias = Literal[
    "GENERAL_PURPOSE",
    "INTUNE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GENERAL_PURPOSE",
        "INTUNE",
    )
)


def serialize_json(value: ConnectorType) -> str:
    return value


def deserialize_json(data: str) -> ConnectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorType value: {data!r}")
    return cast(ConnectorType, data)
