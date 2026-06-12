"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#DeleteRecordRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.deletion_mode
    import aws_sdk_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import aws_sdk_sagemaker_featurestore_runtime.types.target_stores
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string


class DeleteRecordRequest(TypedDict):
    feature_group_name: "aws_sdk_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the feature group to delete the record from. </p>"""
    record_identifier_value_as_string: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The value for the <code>RecordIdentifier</code> that uniquely identifies the record, in string format. </p>"""
    event_time: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>Timestamp indicating when the deletion event occurred. <code>EventTime</code> can be used to query data at a certain point in time.</p>"""
    target_stores: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.target_stores.TargetStores"
    ]
    """<p>A list of stores from which you're deleting the record. By default, Feature Store deletes the record from all of the stores that you're using for the <code>FeatureGroup</code>.</p>"""
    deletion_mode: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.deletion_mode.DeletionMode"
    ]
    """<p>The name of the deletion mode for deleting the record. By default, the deletion mode is set to <code>SoftDelete</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteRecordRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteRecordRequest:
    out: DeleteRecordRequest = {}  # type: ignore[typeddict-item]
    return out
