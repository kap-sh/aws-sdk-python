"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#BatchGetRecordError``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.message
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string


class BatchGetRecordError(TypedDict):
    feature_group_name: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The name of the feature group that the record belongs to.</p>"""
    record_identifier_value_as_string: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The value for the <code>RecordIdentifier</code> in string format of a Record from a <code>FeatureGroup</code> that is causing an error when attempting to be retrieved.</p>"""
    error_code: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The error code of an error that has occurred when attempting to retrieve a batch of Records. For more information on errors, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_GetRecord.html#API_feature_store_GetRecord_Errors\">Errors</a>.</p>"""
    error_message: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.message.Message"
    ]
    """<p>The error message of an error that has occurred when attempting to retrieve a record in the batch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRecordError) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "record_identifier_value_as_string" in value:
        out["RecordIdentifierValueAsString"] = value[
            "record_identifier_value_as_string"
        ]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> BatchGetRecordError:
    out: BatchGetRecordError = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "RecordIdentifierValueAsString" in data:
        out["record_identifier_value_as_string"] = data["RecordIdentifierValueAsString"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
