"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#FeatureValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker_featurestore_runtime.types.feature_name
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string
    import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string_list


class FeatureValue(TypedDict):
    feature_name: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.feature_name.FeatureName"
    ]
    """<p>The name of a feature that a feature value corresponds to.</p>"""
    value_as_string: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string.ValueAsString"
    ]
    """<p>The value in string format associated with a feature. Used when your <code>CollectionType</code> is <code>None</code>. Note that features types can be <code>String</code>, <code>Integral</code>, or <code>Fractional</code>. This value represents all three types as a string.</p>"""
    value_as_string_list: NotRequired[
        "aws_sdk_sagemaker_featurestore_runtime.types.value_as_string_list.ValueAsStringList"
    ]
    """<p>The list of values in string format associated with a feature. Used when your <code>CollectionType</code> is a <code>List</code>, <code>Set</code>, or <code>Vector</code>. Note that features types can be <code>String</code>, <code>Integral</code>, or <code>Fractional</code>. These values represents all three types as a string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FeatureValue) -> dict:
    out: dict = {}
    if "feature_name" in value:
        out["FeatureName"] = value["feature_name"]
    if "value_as_string" in value:
        out["ValueAsString"] = value["value_as_string"]
    if "value_as_string_list" in value:
        import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string_list

        out["ValueAsStringList"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.value_as_string_list.serialize_json(
                value["value_as_string_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> FeatureValue:
    out: FeatureValue = {}  # type: ignore[typeddict-item]
    if "FeatureName" in data:
        out["feature_name"] = data["FeatureName"]
    if "ValueAsString" in data:
        out["value_as_string"] = data["ValueAsString"]
    if "ValueAsStringList" in data:
        import aws_sdk_sagemaker_featurestore_runtime.types.value_as_string_list

        out["value_as_string_list"] = (
            aws_sdk_sagemaker_featurestore_runtime.types.value_as_string_list.deserialize_json(
                data["ValueAsStringList"]
            )
        )
    return out
