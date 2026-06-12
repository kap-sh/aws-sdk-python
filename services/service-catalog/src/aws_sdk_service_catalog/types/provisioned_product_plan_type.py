"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlanType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProvisionedProductPlanType: TypeAlias = Literal["CLOUDFORMATION",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CLOUDFORMATION",))


def serialize_aws_json_1_1(value: ProvisionedProductPlanType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductPlanType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisionedProductPlanType value: {data!r}"
        )
    return cast(ProvisionedProductPlanType, data)
