"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecordResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_errors
    import capo_sagemaker_featurestore_runtime.types.batch_get_record_result_details
    import capo_sagemaker_featurestore_runtime.types.unprocessed_identifiers


class BatchGetRecordResponse(TypedDict, closed=True):
    records: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.batch_get_record_result_details.BatchGetRecordResultDetails"
    ]
    """<p>A list of Records you requested to be retrieved in batch.</p>"""
    errors: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.batch_get_record_errors.BatchGetRecordErrors"
    ]
    """<p>A list of errors that have occurred when retrieving a batch of Records.</p>"""
    unprocessed_identifiers: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.unprocessed_identifiers.UnprocessedIdentifiers"
    ]
    """<p>A unprocessed list of <code>FeatureGroup</code> names, with their corresponding <code>RecordIdentifier</code> value, and Feature name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRecordResponse) -> dict:
    out: dict = {}
    if "records" in value:
        import capo_sagemaker_featurestore_runtime.types.batch_get_record_result_details

        out["Records"] = (
            capo_sagemaker_featurestore_runtime.types.batch_get_record_result_details.serialize_json(
                value["records"]
            )
        )
    if "errors" in value:
        import capo_sagemaker_featurestore_runtime.types.batch_get_record_errors

        out["Errors"] = (
            capo_sagemaker_featurestore_runtime.types.batch_get_record_errors.serialize_json(
                value["errors"]
            )
        )
    if "unprocessed_identifiers" in value:
        import capo_sagemaker_featurestore_runtime.types.unprocessed_identifiers

        out["UnprocessedIdentifiers"] = (
            capo_sagemaker_featurestore_runtime.types.unprocessed_identifiers.serialize_json(
                value["unprocessed_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetRecordResponse:
    out: BatchGetRecordResponse = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import capo_sagemaker_featurestore_runtime.types.batch_get_record_result_details

        out["records"] = (
            capo_sagemaker_featurestore_runtime.types.batch_get_record_result_details.deserialize_json(
                data["Records"]
            )
        )
    if "Errors" in data:
        import capo_sagemaker_featurestore_runtime.types.batch_get_record_errors

        out["errors"] = (
            capo_sagemaker_featurestore_runtime.types.batch_get_record_errors.deserialize_json(
                data["Errors"]
            )
        )
    if "UnprocessedIdentifiers" in data:
        import capo_sagemaker_featurestore_runtime.types.unprocessed_identifiers

        out["unprocessed_identifiers"] = (
            capo_sagemaker_featurestore_runtime.types.unprocessed_identifiers.deserialize_json(
                data["UnprocessedIdentifiers"]
            )
        )
    return out
