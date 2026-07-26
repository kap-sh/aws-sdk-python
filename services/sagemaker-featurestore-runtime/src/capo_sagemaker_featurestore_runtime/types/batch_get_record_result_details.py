"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecordResultDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_result_detail

BatchGetRecordResultDetails: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.batch_get_record_result_detail.BatchGetRecordResultDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRecordResultDetails) -> list:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_result_detail

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_get_record_result_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchGetRecordResultDetails:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_result_detail

    out: BatchGetRecordResultDetails = []
    for item in data:
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_get_record_result_detail.deserialize_json(
                item
            )
        )
    return out
