"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationResourcePropertyFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.string128

IntegrationResourcePropertyFilterValues: TypeAlias = list[
    "aws_sdk_glue.types.string128.String128"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationResourcePropertyFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IntegrationResourcePropertyFilterValues:
    return list(data)
