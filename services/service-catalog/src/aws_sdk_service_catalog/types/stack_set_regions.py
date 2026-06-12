"""Generated from Smithy shape ``com.amazonaws.servicecatalog#StackSetRegions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.region

StackSetRegions: TypeAlias = list["aws_sdk_service_catalog.types.region.Region"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StackSetRegions) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> StackSetRegions:
    return list(data)
