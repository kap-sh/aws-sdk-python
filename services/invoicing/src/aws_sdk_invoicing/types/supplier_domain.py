"""Generated from Smithy shape ``com.amazonaws.invoicing#SupplierDomain``."""

from typing import Literal, TypeAlias, cast

SupplierDomain: TypeAlias = Literal["NetworkID",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SupplierDomain) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SupplierDomain:
    return cast(SupplierDomain, data)
