"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecordErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_error

BatchGetRecordErrors: TypeAlias = list[
    "aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_error.BatchGetRecordError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRecordErrors) -> list:
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_error.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetRecordErrors:
    import aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_error

    out: BatchGetRecordErrors = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_featurestore_runtime.types.batch_get_record_error.deserialize_json(
                item
            )
        )
    return out
