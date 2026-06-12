"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ServiceActionDefinitionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ServiceActionDefinitionType: TypeAlias = Literal["SSM_AUTOMATION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SSM_AUTOMATION",))


def serialize_aws_json_1_1(value: ServiceActionDefinitionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceActionDefinitionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ServiceActionDefinitionType value: {data!r}"
        )
    return cast(ServiceActionDefinitionType, data)
