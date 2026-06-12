"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateFeatureGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.feature_additions
    import aws_sdk_sagemaker.types.feature_group_name_or_arn
    import aws_sdk_sagemaker.types.online_store_config_update
    import aws_sdk_sagemaker.types.throughput_config_update


class UpdateFeatureGroupRequest(TypedDict):
    feature_group_name: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_name_or_arn.FeatureGroupNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the feature group that you're updating.</p>"""
    feature_additions: NotRequired[
        "aws_sdk_sagemaker.types.feature_additions.FeatureAdditions"
    ]
    """<p>Updates the feature group. Updating a feature group is an asynchronous operation. When you get an HTTP 200 response, you've made a valid request. It takes some time after you've made a valid request for Feature Store to update the feature group.</p>"""
    online_store_config: NotRequired[
        "aws_sdk_sagemaker.types.online_store_config_update.OnlineStoreConfigUpdate"
    ]
    """<p>Updates the feature group online store configuration.</p>"""
    throughput_config: NotRequired[
        "aws_sdk_sagemaker.types.throughput_config_update.ThroughputConfigUpdate"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFeatureGroupRequest) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "feature_additions" in value:
        import aws_sdk_sagemaker.types.feature_additions

        out["FeatureAdditions"] = (
            aws_sdk_sagemaker.types.feature_additions.serialize_aws_json_1_1(
                value["feature_additions"]
            )
        )
    if "online_store_config" in value:
        import aws_sdk_sagemaker.types.online_store_config_update

        out["OnlineStoreConfig"] = (
            aws_sdk_sagemaker.types.online_store_config_update.serialize_aws_json_1_1(
                value["online_store_config"]
            )
        )
    if "throughput_config" in value:
        import aws_sdk_sagemaker.types.throughput_config_update

        out["ThroughputConfig"] = (
            aws_sdk_sagemaker.types.throughput_config_update.serialize_aws_json_1_1(
                value["throughput_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFeatureGroupRequest:
    out: UpdateFeatureGroupRequest = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "FeatureAdditions" in data:
        import aws_sdk_sagemaker.types.feature_additions

        out["feature_additions"] = (
            aws_sdk_sagemaker.types.feature_additions.deserialize_aws_json_1_1(
                data["FeatureAdditions"]
            )
        )
    if "OnlineStoreConfig" in data:
        import aws_sdk_sagemaker.types.online_store_config_update

        out["online_store_config"] = (
            aws_sdk_sagemaker.types.online_store_config_update.deserialize_aws_json_1_1(
                data["OnlineStoreConfig"]
            )
        )
    if "ThroughputConfig" in data:
        import aws_sdk_sagemaker.types.throughput_config_update

        out["throughput_config"] = (
            aws_sdk_sagemaker.types.throughput_config_update.deserialize_aws_json_1_1(
                data["ThroughputConfig"]
            )
        )
    return out
