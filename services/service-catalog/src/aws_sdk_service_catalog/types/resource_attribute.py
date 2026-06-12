"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ResourceAttribute``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ResourceAttribute: TypeAlias = Literal[
    "PROPERTIES",
    "METADATA",
    "CREATIONPOLICY",
    "UPDATEPOLICY",
    "DELETIONPOLICY",
    "TAGS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROPERTIES",
        "METADATA",
        "CREATIONPOLICY",
        "UPDATEPOLICY",
        "DELETIONPOLICY",
        "TAGS",
    )
)


def serialize_aws_json_1_1(value: ResourceAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceAttribute:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceAttribute value: {data!r}")
    return cast(ResourceAttribute, data)
