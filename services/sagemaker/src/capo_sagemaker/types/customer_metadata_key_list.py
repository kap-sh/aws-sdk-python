"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomerMetadataKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.customer_metadata_key

CustomerMetadataKeyList: TypeAlias = list[
    "capo_sagemaker.types.customer_metadata_key.CustomerMetadataKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerMetadataKeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> CustomerMetadataKeyList:
    return list(data)
