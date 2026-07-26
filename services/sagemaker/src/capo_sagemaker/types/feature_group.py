"""Generated from Smithy shape ``com.amazonaws.sagemaker#FeatureGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.description
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.feature_definitions
    import capo_sagemaker.types.feature_group_arn
    import capo_sagemaker.types.feature_group_name
    import capo_sagemaker.types.feature_group_status
    import capo_sagemaker.types.feature_name
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.last_update_status
    import capo_sagemaker.types.offline_store_config
    import capo_sagemaker.types.offline_store_status
    import capo_sagemaker.types.online_store_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.tag_list


class FeatureGroup(TypedDict, closed=True):
    feature_group_arn: NotRequired[
        "capo_sagemaker.types.feature_group_arn.FeatureGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a <code>FeatureGroup</code>.</p>"""
    feature_group_name: NotRequired[
        "capo_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>The name of the <code>FeatureGroup</code>.</p>"""
    record_identifier_feature_name: NotRequired[
        "capo_sagemaker.types.feature_name.FeatureName"
    ]
    """<p>The name of the <code>Feature</code> whose value uniquely identifies a <code>Record</code> defined in the <code>FeatureGroup</code> <code>FeatureDefinitions</code>.</p>"""
    event_time_feature_name: NotRequired[
        "capo_sagemaker.types.feature_name.FeatureName"
    ]
    """<p>The name of the feature that stores the <code>EventTime</code> of a Record in a <code>FeatureGroup</code>.</p> <p>A <code>EventTime</code> is point in time when a new event occurs that corresponds to the creation or update of a <code>Record</code> in <code>FeatureGroup</code>. All <code>Records</code> in the <code>FeatureGroup</code> must have a corresponding <code>EventTime</code>.</p>"""
    feature_definitions: NotRequired[
        "capo_sagemaker.types.feature_definitions.FeatureDefinitions"
    ]
    """<p>A list of <code>Feature</code>s. Each <code>Feature</code> must include a <code>FeatureName</code> and a <code>FeatureType</code>. </p> <p>Valid <code>FeatureType</code>s are <code>Integral</code>, <code>Fractional</code> and <code>String</code>. </p> <p> <code>FeatureName</code>s cannot be any of the following: <code>is_deleted</code>, <code>write_time</code>, <code>api_invocation_time</code>.</p> <p>You can create up to 2,500 <code>FeatureDefinition</code>s per <code>FeatureGroup</code>.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The time a <code>FeatureGroup</code> was created.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp indicating the last time you updated the feature group.</p>"""
    online_store_config: NotRequired[
        "capo_sagemaker.types.online_store_config.OnlineStoreConfig"
    ]
    offline_store_config: NotRequired[
        "capo_sagemaker.types.offline_store_config.OfflineStoreConfig"
    ]
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM execution role used to create the feature group.</p>"""
    feature_group_status: NotRequired[
        "capo_sagemaker.types.feature_group_status.FeatureGroupStatus"
    ]
    """<p>A <code>FeatureGroup</code> status.</p>"""
    offline_store_status: NotRequired[
        "capo_sagemaker.types.offline_store_status.OfflineStoreStatus"
    ]
    last_update_status: NotRequired[
        "capo_sagemaker.types.last_update_status.LastUpdateStatus"
    ]
    """<p>A value that indicates whether the feature group was updated successfully.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>The reason that the <code>FeatureGroup</code> failed to be replicated in the <code>OfflineStore</code>. This is failure may be due to a failure to create a <code>FeatureGroup</code> in or delete a <code>FeatureGroup</code> from the <code>OfflineStore</code>.</p>"""
    description: NotRequired["capo_sagemaker.types.description.Description"]
    """<p>A free form description of a <code>FeatureGroup</code>.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Tags used to define a <code>FeatureGroup</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureGroup) -> dict:
    out: dict = {}
    if "feature_group_arn" in value:
        out["FeatureGroupArn"] = value["feature_group_arn"]
    if "feature_group_name" in value:
        out["FeatureGroupName"] = value["feature_group_name"]
    if "record_identifier_feature_name" in value:
        out["RecordIdentifierFeatureName"] = value["record_identifier_feature_name"]
    if "event_time_feature_name" in value:
        out["EventTimeFeatureName"] = value["event_time_feature_name"]
    if "feature_definitions" in value:
        import capo_sagemaker.types.feature_definitions

        out["FeatureDefinitions"] = (
            capo_sagemaker.types.feature_definitions.serialize_aws_json_1_1(
                value["feature_definitions"]
            )
        )
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "online_store_config" in value:
        import capo_sagemaker.types.online_store_config

        out["OnlineStoreConfig"] = (
            capo_sagemaker.types.online_store_config.serialize_aws_json_1_1(
                value["online_store_config"]
            )
        )
    if "offline_store_config" in value:
        import capo_sagemaker.types.offline_store_config

        out["OfflineStoreConfig"] = (
            capo_sagemaker.types.offline_store_config.serialize_aws_json_1_1(
                value["offline_store_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
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
    if "last_update_status" in value:
        import capo_sagemaker.types.last_update_status

        out["LastUpdateStatus"] = (
            capo_sagemaker.types.last_update_status.serialize_aws_json_1_1(
                value["last_update_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureGroup:
    out: FeatureGroup = {}  # type: ignore[typeddict-item]
    if "FeatureGroupArn" in data:
        out["feature_group_arn"] = data["FeatureGroupArn"]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "RecordIdentifierFeatureName" in data:
        out["record_identifier_feature_name"] = data["RecordIdentifierFeatureName"]
    if "EventTimeFeatureName" in data:
        out["event_time_feature_name"] = data["EventTimeFeatureName"]
    if "FeatureDefinitions" in data:
        import capo_sagemaker.types.feature_definitions

        out["feature_definitions"] = (
            capo_sagemaker.types.feature_definitions.deserialize_aws_json_1_1(
                data["FeatureDefinitions"]
            )
        )
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "OnlineStoreConfig" in data:
        import capo_sagemaker.types.online_store_config

        out["online_store_config"] = (
            capo_sagemaker.types.online_store_config.deserialize_aws_json_1_1(
                data["OnlineStoreConfig"]
            )
        )
    if "OfflineStoreConfig" in data:
        import capo_sagemaker.types.offline_store_config

        out["offline_store_config"] = (
            capo_sagemaker.types.offline_store_config.deserialize_aws_json_1_1(
                data["OfflineStoreConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
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
    if "LastUpdateStatus" in data:
        import capo_sagemaker.types.last_update_status

        out["last_update_status"] = (
            capo_sagemaker.types.last_update_status.deserialize_aws_json_1_1(
                data["LastUpdateStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
