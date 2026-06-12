"""Generated from Smithy shape ``com.amazonaws.devopsguru#OrganizationResourceCollectionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_devops_guru.errors import DeserializationError

OrganizationResourceCollectionType: TypeAlias = Literal[
    "AWS_CLOUD_FORMATION",
    "AWS_SERVICE",
    "AWS_ACCOUNT",
    "AWS_TAGS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS_CLOUD_FORMATION",
        "AWS_SERVICE",
        "AWS_ACCOUNT",
        "AWS_TAGS",
    )
)


def serialize_json(value: OrganizationResourceCollectionType) -> str:
    return value


def deserialize_json(data: str) -> OrganizationResourceCollectionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OrganizationResourceCollectionType value: {data!r}"
        )
    return cast(OrganizationResourceCollectionType, data)
