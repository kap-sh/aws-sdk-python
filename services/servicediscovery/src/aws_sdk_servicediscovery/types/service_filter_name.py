"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ServiceFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_servicediscovery.errors import DeserializationError

ServiceFilterName: TypeAlias = Literal[
    "NAMESPACE_ID",
    "RESOURCE_OWNER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NAMESPACE_ID",
        "RESOURCE_OWNER",
    )
)


def serialize_aws_json_1_1(value: ServiceFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceFilterName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceFilterName value: {data!r}")
    return cast(ServiceFilterName, data)
