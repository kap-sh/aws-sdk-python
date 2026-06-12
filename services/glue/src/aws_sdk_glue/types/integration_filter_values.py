"""Generated from Smithy shape ``com.amazonaws.glue#IntegrationFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.string128

IntegrationFilterValues: TypeAlias = list["aws_sdk_glue.types.string128.String128"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IntegrationFilterValues:
    return list(data)
