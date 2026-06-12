"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductViewFilterBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProvisionedProductViewFilterBy: TypeAlias = Literal["SearchQuery",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("SearchQuery",))


def serialize_aws_json_1_1(value: ProvisionedProductViewFilterBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisionedProductViewFilterBy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisionedProductViewFilterBy value: {data!r}"
        )
    return cast(ProvisionedProductViewFilterBy, data)
