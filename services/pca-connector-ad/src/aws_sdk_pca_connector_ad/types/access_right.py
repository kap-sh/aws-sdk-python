"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#AccessRight``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

AccessRight: TypeAlias = Literal[
    "ALLOW",
    "DENY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOW",
        "DENY",
    )
)


def serialize_json(value: AccessRight) -> str:
    return value


def deserialize_json(data: str) -> AccessRight:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccessRight value: {data!r}")
    return cast(AccessRight, data)
