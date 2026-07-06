"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.collection_config
    import aws_sdk_sagemaker.types.collection_type
    import aws_sdk_sagemaker.types.feature_name
    import aws_sdk_sagemaker.types.feature_type


class FeatureDefinition(TypedDict, closed=True):
    feature_name: NotRequired["aws_sdk_sagemaker.types.feature_name.FeatureName"]
    """<p>The name of a feature. The type must be a string. <code>FeatureName</code> cannot be any of the following: <code>is_deleted</code>, <code>write_time</code>, <code>api_invocation_time</code>.</p> <p>The name:</p> <ul> <li> <p>Must start with an alphanumeric character.</p> </li> <li> <p>Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.</p> </li> </ul>"""
    feature_type: NotRequired["aws_sdk_sagemaker.types.feature_type.FeatureType"]
    """<p>The value type of a feature. Valid values are Integral, Fractional, or String.</p>"""
    collection_type: NotRequired[
        "aws_sdk_sagemaker.types.collection_type.CollectionType"
    ]
    """<p>A grouping of elements where each element within the collection must have the same feature type (<code>String</code>, <code>Integral</code>, or <code>Fractional</code>).</p> <ul> <li> <p> <code>List</code>: An ordered collection of elements.</p> </li> <li> <p> <code>Set</code>: An unordered collection of unique elements.</p> </li> <li> <p> <code>Vector</code>: A specialized list that represents a fixed-size array of elements. The vector dimension is determined by you. Must have elements with fractional feature types. </p> </li> </ul>"""
    collection_config: NotRequired[
        "aws_sdk_sagemaker.types.collection_config.CollectionConfig"
    ]
    """<p>Configuration for your collection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureDefinition) -> dict:
    out: dict = {}
    if "feature_name" in value:
        out["FeatureName"] = value["feature_name"]
    if "feature_type" in value:
        import aws_sdk_sagemaker.types.feature_type

        out["FeatureType"] = (
            aws_sdk_sagemaker.types.feature_type.serialize_aws_json_1_1(
                value["feature_type"]
            )
        )
    if "collection_type" in value:
        import aws_sdk_sagemaker.types.collection_type

        out["CollectionType"] = (
            aws_sdk_sagemaker.types.collection_type.serialize_aws_json_1_1(
                value["collection_type"]
            )
        )
    if "collection_config" in value:
        import aws_sdk_sagemaker.types.collection_config

        out["CollectionConfig"] = (
            aws_sdk_sagemaker.types.collection_config.serialize_aws_json_1_1(
                value["collection_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureDefinition:
    out: FeatureDefinition = {}  # type: ignore[typeddict-item]
    if "FeatureName" in data:
        out["feature_name"] = data["FeatureName"]
    if "FeatureType" in data:
        import aws_sdk_sagemaker.types.feature_type

        out["feature_type"] = (
            aws_sdk_sagemaker.types.feature_type.deserialize_aws_json_1_1(
                data["FeatureType"]
            )
        )
    if "CollectionType" in data:
        import aws_sdk_sagemaker.types.collection_type

        out["collection_type"] = (
            aws_sdk_sagemaker.types.collection_type.deserialize_aws_json_1_1(
                data["CollectionType"]
            )
        )
    if "CollectionConfig" in data:
        import aws_sdk_sagemaker.types.collection_config

        out["collection_config"] = (
            aws_sdk_sagemaker.types.collection_config.deserialize_aws_json_1_1(
                data["CollectionConfig"]
            )
        )
    return out
