"""Generated from Smithy shape ``com.amazonaws.servicequotas#InputTagKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.tag_key

InputTagKeys: TypeAlias = list["aws_sdk_service_quotas.types.tag_key.TagKey"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputTagKeys) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> InputTagKeys:
    return list(data)
