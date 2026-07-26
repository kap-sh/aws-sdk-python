"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#UnprocessedIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_identifier

UnprocessedIdentifiers: TypeAlias = list[
    "capo_sagemaker_featurestore_runtime.types.batch_get_record_identifier.BatchGetRecordIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedIdentifiers) -> list:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_identifier

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_get_record_identifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UnprocessedIdentifiers:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_identifier

    out: UnprocessedIdentifiers = []
    for item in data:
        out.append(
            capo_sagemaker_featurestore_runtime.types.batch_get_record_identifier.deserialize_json(
                item
            )
        )
    return out
