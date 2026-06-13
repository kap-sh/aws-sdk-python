"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ConnectorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_scep.errors import DeserializationError

ConnectorStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "DELETING",
        "FAILED",
    )
)


def serialize_json(value: ConnectorStatus) -> str:
    return value


def deserialize_json(data: str) -> ConnectorStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConnectorStatus value: {data!r}")
    return cast(ConnectorStatus, data)
