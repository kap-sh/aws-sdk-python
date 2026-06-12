"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#AssociationOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog_appregistry.errors import DeserializationError

AssociationOption: TypeAlias = Literal[
    "APPLY_APPLICATION_TAG",
    "SKIP_APPLICATION_TAG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "APPLY_APPLICATION_TAG",
        "SKIP_APPLICATION_TAG",
    )
)


def serialize_json(value: AssociationOption) -> str:
    return value


def deserialize_json(data: str) -> AssociationOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationOption value: {data!r}")
    return cast(AssociationOption, data)
