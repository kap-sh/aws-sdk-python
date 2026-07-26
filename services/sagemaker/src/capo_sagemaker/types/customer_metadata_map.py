"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomerMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.customer_metadata_key
    import capo_sagemaker.types.customer_metadata_value

CustomerMetadataMap: TypeAlias = dict[
    "capo_sagemaker.types.customer_metadata_key.CustomerMetadataKey",
    "capo_sagemaker.types.customer_metadata_value.CustomerMetadataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CustomerMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerMetadataMap:
    out: CustomerMetadataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
