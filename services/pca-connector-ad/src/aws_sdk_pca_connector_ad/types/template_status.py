"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#TemplateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

TemplateStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
    )
)


def serialize_json(value: TemplateStatus) -> str:
    return value


def deserialize_json(data: str) -> TemplateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TemplateStatus value: {data!r}")
    return cast(TemplateStatus, data)
