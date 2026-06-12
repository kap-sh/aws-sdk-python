"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecordResultDetail``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.expires_at
    import aws_sdk_sagemaker_featurestore_runtime.types.record
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string


class BatchGetRecordResultDetail(TypedDict):
    feature_group_name: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The <code>FeatureGroupName</code> containing Records you retrieved in a batch.</p>"""
    record_identifier_value_as_string: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The value of the record identifier in string format.</p>"""
    record: NotRequired["aws_sdk_sagemaker_featurestore_runtime.types.record.Record"]
    """<p>The <code>Record</code> retrieved.</p>"""
    expires_at: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.expires_at.ExpiresAt"
    ]
    """<p>The <code>ExpiresAt</code> ISO string of the requested record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRecordResultDetail) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "record_identifier_value_as_string" in value:
        out["RecordIdentifierValueAsString"] = value[
            "record_identifier_value_as_string"
        ]
    if "record" in value:
        import aws_sdk_sagemaker_featurestore_runtime.types.record

        out["Record"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.record.serialize_json(
                value["record"]
            )
        )
    if "expires_at" in value:
        out["ExpiresAt"] = value["expires_at"]
    return out


def deserialize_json(data: dict) -> BatchGetRecordResultDetail:
    out: BatchGetRecordResultDetail = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "RecordIdentifierValueAsString" in data:
        out["record_identifier_value_as_string"] = data["RecordIdentifierValueAsString"]
    if "Record" in data:
        import aws_sdk_sagemaker_featurestore_runtime.types.record

        out["record"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.record.deserialize_json(
                data["Record"]
            )
        )
    if "ExpiresAt" in data:
        out["expires_at"] = data["ExpiresAt"]
    return out
