"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_group_arn
    import capo_sagemaker.types.feature_group_name
    import capo_sagemaker.types.feature_group_status
    import capo_sagemaker.types.offline_store_status
    import capo_sagemaker.types.timestamp


class FeatureGroupSummary(TypedDict, closed=True):
    feature_group_name: NotRequired[
        "capo_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>The name of <code>FeatureGroup</code>.</p>"""
    feature_group_arn: NotRequired[
        "capo_sagemaker.types.feature_group_arn.FeatureGroupArn"
    ]
    """<p>Unique identifier for the <code>FeatureGroup</code>.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp indicating the time of creation time of the <code>FeatureGroup</code>.</p>"""
    feature_group_status: NotRequired[
        "capo_sagemaker.types.feature_group_status.FeatureGroupStatus"
    ]
    """<p>The status of a FeatureGroup. The status can be any of the following: <code>Creating</code>, <code>Created</code>, <code>CreateFail</code>, <code>Deleting</code> or <code>DetailFail</code>. </p>"""
    offline_store_status: NotRequired[
        "capo_sagemaker.types.offline_store_status.OfflineStoreStatus"
    ]
    """<p>Notifies you if replicating data into the <code>OfflineStore</code> has failed. Returns either: <code>Active</code> or <code>Blocked</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureGroupSummary) -> dict:
    out: dict = {}
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "feature_group_arn" in value:
        out["FeatureGroupArn"] = value["feature_group_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "feature_group_status" in value:
        import capo_sagemaker.types.feature_group_status

        out["FeatureGroupStatus"] = (
            capo_sagemaker.types.feature_group_status.serialize_aws_json_1_1(
                value["feature_group_status"]
            )
        )
    if "offline_store_status" in value:
        import capo_sagemaker.types.offline_store_status

        out["OfflineStoreStatus"] = (
            capo_sagemaker.types.offline_store_status.serialize_aws_json_1_1(
                value["offline_store_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureGroupSummary:
    out: FeatureGroupSummary = {}  # type: ignore[typeddict-item]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "FeatureGroupArn" in data:
        out["feature_group_arn"] = data["FeatureGroupArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "FeatureGroupStatus" in data:
        import capo_sagemaker.types.feature_group_status

        out["feature_group_status"] = (
            capo_sagemaker.types.feature_group_status.deserialize_aws_json_1_1(
                data["FeatureGroupStatus"]
            )
        )
    if "OfflineStoreStatus" in data:
        import capo_sagemaker.types.offline_store_status

        out["offline_store_status"] = (
            capo_sagemaker.types.offline_store_status.deserialize_aws_json_1_1(
                data["OfflineStoreStatus"]
            )
        )
    return out
