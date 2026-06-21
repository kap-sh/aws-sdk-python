"""Generated from Smithy shape ``com.amazonaws.odb#ExternalIdType``."""

from typing import Literal, TypeAlias, cast

ExternalIdType: TypeAlias = Literal[
    "database_ocid",
    "compartment_ocid",
    "tenant_ocid",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExternalIdType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExternalIdType:
    return cast(ExternalIdType, data)
