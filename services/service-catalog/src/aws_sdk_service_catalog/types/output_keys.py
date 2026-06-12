"""Generated from Smithy shape ``com.amazonaws.servicecatalog#OutputKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.output_key

OutputKeys: TypeAlias = list["aws_sdk_service_catalog.types.output_key.OutputKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OutputKeys:
    return list(data)
