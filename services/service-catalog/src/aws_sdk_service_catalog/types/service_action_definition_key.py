"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionDefinitionKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ServiceActionDefinitionKey: TypeAlias = Literal[
    "Name",
    "Version",
    "AssumeRole",
    "Parameters",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "Version",
        "AssumeRole",
        "Parameters",
    )
)


def serialize_aws_json_1_1(value: ServiceActionDefinitionKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceActionDefinitionKey:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceActionDefinitionKey value: {data!r}"
        )
    return cast(ServiceActionDefinitionKey, data)
