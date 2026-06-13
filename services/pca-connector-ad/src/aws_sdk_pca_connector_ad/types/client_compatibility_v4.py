"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ClientCompatibilityV4``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

ClientCompatibilityV4: TypeAlias = Literal[
    "WINDOWS_SERVER_2012",
    "WINDOWS_SERVER_2012_R2",
    "WINDOWS_SERVER_2016",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS_SERVER_2012",
        "WINDOWS_SERVER_2012_R2",
        "WINDOWS_SERVER_2016",
    )
)


def serialize_json(value: ClientCompatibilityV4) -> str:
    return value


def deserialize_json(data: str) -> ClientCompatibilityV4:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClientCompatibilityV4 value: {data!r}")
    return cast(ClientCompatibilityV4, data)
