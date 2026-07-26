"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AllowedValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.string

AllowedValues: TypeAlias = list["capo_service_catalog.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AllowedValues:
    return list(data)
