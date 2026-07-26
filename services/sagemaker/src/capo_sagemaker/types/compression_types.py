"""Generated from Smithy shape ``com.amazonaws.sagemaker#CompressionTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.compression_type

CompressionTypes: TypeAlias = list[
    "capo_sagemaker.types.compression_type.CompressionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompressionTypes) -> list:
    import capo_sagemaker.types.compression_type

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.compression_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CompressionTypes:
    import capo_sagemaker.types.compression_type

    out: CompressionTypes = []
    for item in data:
        out.append(capo_sagemaker.types.compression_type.deserialize_aws_json_1_1(item))
    return out
