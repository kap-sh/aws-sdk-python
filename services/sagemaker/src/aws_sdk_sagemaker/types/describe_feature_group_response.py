"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeFeatureGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.description
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.feature_definitions
    import aws_sdk_sagemaker.types.feature_group_arn
    import aws_sdk_sagemaker.types.feature_group_name
    import aws_sdk_sagemaker.types.feature_group_status
    import aws_sdk_sagemaker.types.feature_name
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.last_update_status
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.offline_store_config
    import aws_sdk_sagemaker.types.offline_store_status
    import aws_sdk_sagemaker.types.online_store_config
    import aws_sdk_sagemaker.types.online_store_total_size_bytes
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.throughput_config_description


class DescribeFeatureGroupResponse(TypedDict, closed=True):
    feature_group_arn: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_arn.FeatureGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the <code>FeatureGroup</code>. </p>"""
    feature_group_name: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_name.FeatureGroupName"
    ]
    """<p>he name of the <code>FeatureGroup</code>.</p>"""
    record_identifier_feature_name: NotRequired[
        "aws_sdk_sagemaker.types.feature_name.FeatureName"
    ]
    """<p>The name of the <code>Feature</code> used for <code>RecordIdentifier</code>, whose value uniquely identifies a record stored in the feature store.</p>"""
    event_time_feature_name: NotRequired[
        "aws_sdk_sagemaker.types.feature_name.FeatureName"
    ]
    """<p>The name of the feature that stores the <code>EventTime</code> of a Record in a <code>FeatureGroup</code>.</p> <p> An <code>EventTime</code> is a point in time when a new event occurs that corresponds to the creation or update of a <code>Record</code> in a <code>FeatureGroup</code>. All <code>Records</code> in the <code>FeatureGroup</code> have a corresponding <code>EventTime</code>.</p>"""
    feature_definitions: NotRequired[
        "aws_sdk_sagemaker.types.feature_definitions.FeatureDefinitions"
    ]
    """<p>A list of the <code>Features</code> in the <code>FeatureGroup</code>. Each feature is defined by a <code>FeatureName</code> and <code>FeatureType</code>.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp indicating when SageMaker created the <code>FeatureGroup</code>.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp indicating when the feature group was last updated.</p>"""
    online_store_config: NotRequired[
        "aws_sdk_sagemaker.types.online_store_config.OnlineStoreConfig"
    ]
    """<p>The configuration for the <code>OnlineStore</code>.</p>"""
    offline_store_config: NotRequired[
        "aws_sdk_sagemaker.types.offline_store_config.OfflineStoreConfig"
    ]
    """<p>The configuration of the offline store. It includes the following configurations:</p> <ul> <li> <p>Amazon S3 location of the offline store.</p> </li> <li> <p>Configuration of the Glue data catalog.</p> </li> <li> <p>Table format of the offline store.</p> </li> <li> <p>Option to disable the automatic creation of a Glue table for the offline store.</p> </li> <li> <p>Encryption configuration.</p> </li> </ul>"""
    throughput_config: NotRequired[
        "aws_sdk_sagemaker.types.throughput_config_description.ThroughputConfigDescription"
    ]
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM execution role used to persist data into the OfflineStore if an OfflineStoreConfig is provided.</p>"""
    feature_group_status: NotRequired[
        "aws_sdk_sagemaker.types.feature_group_status.FeatureGroupStatus"
    ]
    """<p>The status of the feature group.</p>"""
    offline_store_status: NotRequired[
        "aws_sdk_sagemaker.types.offline_store_status.OfflineStoreStatus"
    ]
    """<p>The status of the <code>OfflineStore</code>. Notifies you if replicating data into the <code>OfflineStore</code> has failed. Returns either: <code>Active</code> or <code>Blocked</code> </p>"""
    last_update_status: NotRequired[
        "aws_sdk_sagemaker.types.last_update_status.LastUpdateStatus"
    ]
    """<p>A value indicating whether the update made to the feature group was successful.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The reason that the <code>FeatureGroup</code> failed to be replicated in the <code>OfflineStore</code>. This is failure can occur because:</p> <ul> <li> <p>The <code>FeatureGroup</code> could not be created in the <code>OfflineStore</code>.</p> </li> <li> <p>The <code>FeatureGroup</code> could not be deleted from the <code>OfflineStore</code>.</p> </li> </ul>"""
    description: NotRequired["aws_sdk_sagemaker.types.description.Description"]
    """<p>A free form description of the feature group.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination of the list of <code>Features</code> (<code>FeatureDefinitions</code>).</p>"""
    online_store_total_size_bytes: NotRequired[
        "aws_sdk_sagemaker.types.online_store_total_size_bytes.OnlineStoreTotalSizeBytes"
    ]
    """<p>The size of the <code>OnlineStore</code> in bytes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFeatureGroupResponse) -> dict:
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
        import aws_sdk_sagemaker.types.feature_definitions

        out["FeatureDefinitions"] = (
            aws_sdk_sagemaker.types.feature_definitions.serialize_aws_json_1_1(
                value["feature_definitions"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "online_store_config" in value:
        import aws_sdk_sagemaker.types.online_store_config

        out["OnlineStoreConfig"] = (
            aws_sdk_sagemaker.types.online_store_config.serialize_aws_json_1_1(
                value["online_store_config"]
            )
        )
    if "offline_store_config" in value:
        import aws_sdk_sagemaker.types.offline_store_config

        out["OfflineStoreConfig"] = (
            aws_sdk_sagemaker.types.offline_store_config.serialize_aws_json_1_1(
                value["offline_store_config"]
            )
        )
    if "throughput_config" in value:
        import aws_sdk_sagemaker.types.throughput_config_description

        out["ThroughputConfig"] = (
            aws_sdk_sagemaker.types.throughput_config_description.serialize_aws_json_1_1(
                value["throughput_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "feature_group_status" in value:
        import aws_sdk_sagemaker.types.feature_group_status

        out["FeatureGroupStatus"] = (
            aws_sdk_sagemaker.types.feature_group_status.serialize_aws_json_1_1(
                value["feature_group_status"]
            )
        )
    if "offline_store_status" in value:
        import aws_sdk_sagemaker.types.offline_store_status

        out["OfflineStoreStatus"] = (
            aws_sdk_sagemaker.types.offline_store_status.serialize_aws_json_1_1(
                value["offline_store_status"]
            )
        )
    if "last_update_status" in value:
        import aws_sdk_sagemaker.types.last_update_status

        out["LastUpdateStatus"] = (
            aws_sdk_sagemaker.types.last_update_status.serialize_aws_json_1_1(
                value["last_update_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "description" in value:
        out["Description"] = value["description"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "online_store_total_size_bytes" in value:
        out["OnlineStoreTotalSizeBytes"] = value["online_store_total_size_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFeatureGroupResponse:
    out: DescribeFeatureGroupResponse = {}  # type: ignore[typeddict-item]
    if "FeatureGroupArn" in data:
        out["feature_group_arn"] = data["FeatureGroupArn"]
    if "FeatureGroupName" in data:
        out["feature_group_name"] = data["FeatureGroupName"]
    if "RecordIdentifierFeatureName" in data:
        out["record_identifier_feature_name"] = data["RecordIdentifierFeatureName"]
    if "EventTimeFeatureName" in data:
        out["event_time_feature_name"] = data["EventTimeFeatureName"]
    if "FeatureDefinitions" in data:
        import aws_sdk_sagemaker.types.feature_definitions

        out["feature_definitions"] = (
            aws_sdk_sagemaker.types.feature_definitions.deserialize_aws_json_1_1(
                data["FeatureDefinitions"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "OnlineStoreConfig" in data:
        import aws_sdk_sagemaker.types.online_store_config

        out["online_store_config"] = (
            aws_sdk_sagemaker.types.online_store_config.deserialize_aws_json_1_1(
                data["OnlineStoreConfig"]
            )
        )
    if "OfflineStoreConfig" in data:
        import aws_sdk_sagemaker.types.offline_store_config

        out["offline_store_config"] = (
            aws_sdk_sagemaker.types.offline_store_config.deserialize_aws_json_1_1(
                data["OfflineStoreConfig"]
            )
        )
    if "ThroughputConfig" in data:
        import aws_sdk_sagemaker.types.throughput_config_description

        out["throughput_config"] = (
            aws_sdk_sagemaker.types.throughput_config_description.deserialize_aws_json_1_1(
                data["ThroughputConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "FeatureGroupStatus" in data:
        import aws_sdk_sagemaker.types.feature_group_status

        out["feature_group_status"] = (
            aws_sdk_sagemaker.types.feature_group_status.deserialize_aws_json_1_1(
                data["FeatureGroupStatus"]
            )
        )
    if "OfflineStoreStatus" in data:
        import aws_sdk_sagemaker.types.offline_store_status

        out["offline_store_status"] = (
            aws_sdk_sagemaker.types.offline_store_status.deserialize_aws_json_1_1(
                data["OfflineStoreStatus"]
            )
        )
    if "LastUpdateStatus" in data:
        import aws_sdk_sagemaker.types.last_update_status

        out["last_update_status"] = (
            aws_sdk_sagemaker.types.last_update_status.deserialize_aws_json_1_1(
                data["LastUpdateStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "OnlineStoreTotalSizeBytes" in data:
        out["online_store_total_size_bytes"] = data["OnlineStoreTotalSizeBytes"]
    return out
