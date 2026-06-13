"""Generated from Smithy shape ``com.amazonaws.invoicing#SupplierDomain``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_invoicing.errors import DeserializationError

SupplierDomain: TypeAlias = Literal["NetworkID",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("NetworkID",))


def serialize_aws_json_1_0(value: SupplierDomain) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SupplierDomain:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SupplierDomain value: {data!r}")
    return cast(SupplierDomain, data)
