"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProductSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProductSource: TypeAlias = Literal["ACCOUNT",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ACCOUNT",))


def serialize_aws_json_1_1(value: ProductSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProductSource value: {data!r}")
    return cast(ProductSource, data)
