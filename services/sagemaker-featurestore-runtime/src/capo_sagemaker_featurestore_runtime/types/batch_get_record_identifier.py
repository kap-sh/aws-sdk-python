"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecordIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import capo_sagemaker_featurestore_runtime.types.feature_names
    import capo_sagemaker_featurestore_runtime.types.record_identifiers


class BatchGetRecordIdentifier(TypedDict, closed=True):
    feature_group_name: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the <code>FeatureGroup</code> containing the records you are retrieving in a batch.</p>"""
    record_identifiers_value_as_string: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.record_identifiers.RecordIdentifiers"
    ]
    """<p>The value for a list of record identifiers in string format.</p>"""
    feature_names: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.feature_names.FeatureNames"
    ]
    """<p>List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRecordIdentifier) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "record_identifiers_value_as_string" in value:
        import capo_sagemaker_featurestore_runtime.types.record_identifiers

        out["RecordIdentifiersValueAsString"] = (
            capo_sagemaker_featurestore_runtime.types.record_identifiers.serialize_json(
                value["record_identifiers_value_as_string"]
            )
        )
    if "feature_names" in value:
        import capo_sagemaker_featurestore_runtime.types.feature_names

        out["FeatureNames"] = (
            capo_sagemaker_featurestore_runtime.types.feature_names.serialize_json(
                value["feature_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetRecordIdentifier:
    out: BatchGetRecordIdentifier = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "RecordIdentifiersValueAsString" in data:
        import capo_sagemaker_featurestore_runtime.types.record_identifiers

        out["record_identifiers_value_as_string"] = (
            capo_sagemaker_featurestore_runtime.types.record_identifiers.deserialize_json(
                data["RecordIdentifiersValueAsString"]
            )
        )
    if "FeatureNames" in data:
        import capo_sagemaker_featurestore_runtime.types.feature_names

        out["feature_names"] = (
            capo_sagemaker_featurestore_runtime.types.feature_names.deserialize_json(
                data["FeatureNames"]
            )
        )
    return out
