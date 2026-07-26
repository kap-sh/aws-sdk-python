"""Generated from Smithy shape ``com.amazonaws.devopsguru#OrganizationResourceCollectionType``."""

from typing import Literal, TypeAlias, cast

OrganizationResourceCollectionType: TypeAlias = Literal[
    "AWS_CLOUD_FORMATION",
    "AWS_SERVICE",
    "AWS_ACCOUNT",
    "AWS_TAGS",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationResourceCollectionType) -> str:
    return value


def deserialize_json(data: str) -> OrganizationResourceCollectionType:
    return cast(OrganizationResourceCollectionType, data)
