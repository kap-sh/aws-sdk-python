"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#GetRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_featurestore_runtime.types.expiration_time_response
    import capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn
    import capo_sagemaker_featurestore_runtime.types.feature_names
    import capo_sagemaker_featurestore_runtime.types.value_as_string


class GetRecordRequest(TypedDict, closed=True):
    feature_group_name: "capo_sagemaker_featurestore_runtime.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    """<p>The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record.</p>"""
    record_identifier_value_as_string: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The value that corresponds to <code>RecordIdentifier</code> type and uniquely identifies the record in the <code>FeatureGroup</code>. </p>"""
    feature_names: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.feature_names.FeatureNames"
    ]
    """<p>List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.</p>"""
    expiration_time_response: NotRequired[
        "capo_sagemaker_featurestore_runtime.types.expiration_time_response.ExpirationTimeResponse"
    ]
    """<p>Parameter to request <code>ExpiresAt</code> in response. If <code>Enabled</code>, <code>GetRecord</code> will return the value of <code>ExpiresAt</code>, if it is not null. If <code>Disabled</code> and null, <code>GetRecord</code> will return null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecordRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRecordRequest:
    out: GetRecordRequest = {}  # type: ignore[typeddict-item]
    return out
