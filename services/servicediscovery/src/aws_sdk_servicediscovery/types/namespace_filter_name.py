"""Generated from Smithy shape ``com.amazonaws.servicediscovery#NamespaceFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

NamespaceFilterName: TypeAlias = Literal[
    "TYPE",
    "NAME",
    "HTTP_NAME",
    "RESOURCE_OWNER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TYPE",
        "NAME",
        "HTTP_NAME",
        "RESOURCE_OWNER",
    )
)


def serialize_aws_json_1_1(value: NamespaceFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamespaceFilterName value: {data!r}")
    return cast(NamespaceFilterName, data)
