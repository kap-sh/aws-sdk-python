"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.arn
    import aws_sdk_config_service.types.availability_zone
    import aws_sdk_config_service.types.aws_region
    import aws_sdk_config_service.types.configuration
    import aws_sdk_config_service.types.configuration_item_capture_time
    import aws_sdk_config_service.types.configuration_item_delivery_time
    import aws_sdk_config_service.types.configuration_item_md5_hash
    import aws_sdk_config_service.types.configuration_item_status
    import aws_sdk_config_service.types.configuration_state_id
    import aws_sdk_config_service.types.recording_frequency
    import aws_sdk_config_service.types.related_event_list
    import aws_sdk_config_service.types.relationship_list
    import aws_sdk_config_service.types.resource_creation_time
    import aws_sdk_config_service.types.resource_id
    import aws_sdk_config_service.types.resource_name
    import aws_sdk_config_service.types.resource_type
    import aws_sdk_config_service.types.supplementary_configuration
    import aws_sdk_config_service.types.tags
    import aws_sdk_config_service.types.version


class ConfigurationItem(TypedDict):
    version: NotRequired["aws_sdk_config_service.types.version.Version"]
    """<p>The version number of the resource configuration.</p>"""
    account_id: NotRequired["aws_sdk_config_service.types.account_id.AccountId"]
    """<p>The 12-digit Amazon Web Services account ID associated with the resource.</p>"""
    configuration_item_capture_time: NotRequired[
        "aws_sdk_config_service.types.configuration_item_capture_time.ConfigurationItemCaptureTime"
    ]
    """<p>The time when the recording of configuration changes was initiated for the resource.</p>"""
    configuration_item_status: NotRequired[
        "aws_sdk_config_service.types.configuration_item_status.ConfigurationItemStatus"
    ]
    """<p>The configuration item status. Valid values include:</p> <ul> <li> <p>OK – The resource configuration has been updated</p> </li> <li> <p>ResourceDiscovered – The resource was newly discovered</p> </li> <li> <p>ResourceNotRecorded – The resource was discovered but its configuration was not recorded since the recorder doesn't record resources of this type</p> </li> <li> <p>ResourceDeleted – The resource was deleted</p> </li> <li> <p>ResourceDeletedNotRecorded – The resource was deleted but its configuration was not recorded since the recorder doesn't record resources of this type</p> </li> </ul>"""
    configuration_state_id: NotRequired[
        "aws_sdk_config_service.types.configuration_state_id.ConfigurationStateId"
    ]
    """<p>An identifier that indicates the ordering of the configuration items of a resource.</p>"""
    configuration_item_md5_hash: NotRequired[
        "aws_sdk_config_service.types.configuration_item_md5_hash.ConfigurationItemMD5Hash"
    ]
    """<p>Unique MD5 hash that represents the configuration item's state.</p> <p>You can use MD5 hash to compare the states of two or more configuration items that are associated with the same resource.</p>"""
    arn: NotRequired["aws_sdk_config_service.types.arn.ARN"]
    """<p>Amazon Resource Name (ARN) associated with the resource.</p>"""
    resource_type: NotRequired[
        "aws_sdk_config_service.types.resource_type.ResourceType"
    ]
    """<p>The type of Amazon Web Services resource.</p>"""
    resource_id: NotRequired["aws_sdk_config_service.types.resource_id.ResourceId"]
    """<p>The ID of the resource (for example, <code>sg-xxxxxx</code>).</p>"""
    resource_name: NotRequired[
        "aws_sdk_config_service.types.resource_name.ResourceName"
    ]
    """<p>The custom name of the resource, if available.</p>"""
    aws_region: NotRequired["aws_sdk_config_service.types.aws_region.AwsRegion"]
    """<p>The region where the resource resides.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_config_service.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone associated with the resource.</p>"""
    resource_creation_time: NotRequired[
        "aws_sdk_config_service.types.resource_creation_time.ResourceCreationTime"
    ]
    """<p>The time stamp when the resource was created.</p>"""
    tags: NotRequired["aws_sdk_config_service.types.tags.Tags"]
    """<p>A mapping of key value tags associated with the resource.</p>"""
    related_events: NotRequired[
        "aws_sdk_config_service.types.related_event_list.RelatedEventList"
    ]
    """<p>A list of CloudTrail event IDs.</p> <p>A populated field indicates that the current configuration was initiated by the events recorded in the CloudTrail log. For more information about CloudTrail, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html\">What Is CloudTrail</a>.</p> <p>An empty field indicates that the current configuration was not initiated by any event. As of Version 1.3, the relatedEvents field is empty. You can access the <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_LookupEvents.html\">LookupEvents API</a> in the <i>CloudTrail API Reference</i> to retrieve the events for the resource.</p>"""
    relationships: NotRequired[
        "aws_sdk_config_service.types.relationship_list.RelationshipList"
    ]
    """<p>A list of related Amazon Web Services resources.</p>"""
    configuration: NotRequired[
        "aws_sdk_config_service.types.configuration.Configuration"
    ]
    """<p>A JSON-encoded string that contains the contents for the resource configuration. This string needs to be deserialized using <code>json.loads()</code> before you can access the contents.</p>"""
    supplementary_configuration: NotRequired[
        "aws_sdk_config_service.types.supplementary_configuration.SupplementaryConfiguration"
    ]
    """<p>A string to string map that contains additional contents for the resource configuration.Config returns this field for certain resource types to supplement the information returned for the <code>configuration</code> field.</p> <p>This string to string map needs to be deserialized using <code>json.loads()</code> before you can accessing the contents.</p>"""
    recording_frequency: NotRequired[
        "aws_sdk_config_service.types.recording_frequency.RecordingFrequency"
    ]
    """<p>The recording frequency that Config uses to record configuration changes for the resource.</p> <note> <p>This field only appears in the API response when <code>DAILY</code> recording is enabled for a resource type. If this field is not present, <code>CONTINUOUS</code> recording is enabled for that resource type. For more information on daily recording and continuous recording, see <a href=\"https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-recording-frequency\">Recording Frequency</a> in the <i>Config Developer Guide</i>.</p> </note>"""
    configuration_item_delivery_time: NotRequired[
        "aws_sdk_config_service.types.configuration_item_delivery_time.ConfigurationItemDeliveryTime"
    ]
    """<p>The time when configuration changes for the resource were delivered.</p> <note> <p>This field is optional and is not guaranteed to be present in a configuration item (CI). If you are using daily recording, this field will be populated. However, if you are using continuous recording, this field will be omitted since the delivery time is instantaneous as the CI is available right away.</p> <p>For more information on daily recording and continuous recording, see <a href=\"https://docs.aws.amazon.com/config/latest/developerguide/select-resources.html#select-resources-recording-frequency\">Recording Frequency</a> in the <i>Config Developer Guide</i>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationItem) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "configuration_item_capture_time" in value:
        import aws_sdk_config_service.types.configuration_item_capture_time

        out["configurationItemCaptureTime"] = (
            aws_sdk_config_service.types.configuration_item_capture_time.serialize_aws_json_1_1(
                value["configuration_item_capture_time"]
            )
        )
    if "configuration_item_status" in value:
        import aws_sdk_config_service.types.configuration_item_status

        out["configurationItemStatus"] = (
            aws_sdk_config_service.types.configuration_item_status.serialize_aws_json_1_1(
                value["configuration_item_status"]
            )
        )
    if "configuration_state_id" in value:
        out["configurationStateId"] = value["configuration_state_id"]
    if "configuration_item_md5_hash" in value:
        out["configurationItemMD5Hash"] = value["configuration_item_md5_hash"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "resource_type" in value:
        import aws_sdk_config_service.types.resource_type

        out["resourceType"] = (
            aws_sdk_config_service.types.resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "resource_name" in value:
        out["resourceName"] = value["resource_name"]
    if "aws_region" in value:
        out["awsRegion"] = value["aws_region"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "resource_creation_time" in value:
        import aws_sdk_config_service.types.resource_creation_time

        out["resourceCreationTime"] = (
            aws_sdk_config_service.types.resource_creation_time.serialize_aws_json_1_1(
                value["resource_creation_time"]
            )
        )
    if "tags" in value:
        import aws_sdk_config_service.types.tags

        out["tags"] = aws_sdk_config_service.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "related_events" in value:
        import aws_sdk_config_service.types.related_event_list

        out["relatedEvents"] = (
            aws_sdk_config_service.types.related_event_list.serialize_aws_json_1_1(
                value["related_events"]
            )
        )
    if "relationships" in value:
        import aws_sdk_config_service.types.relationship_list

        out["relationships"] = (
            aws_sdk_config_service.types.relationship_list.serialize_aws_json_1_1(
                value["relationships"]
            )
        )
    if "configuration" in value:
        out["configuration"] = value["configuration"]
    if "supplementary_configuration" in value:
        import aws_sdk_config_service.types.supplementary_configuration

        out["supplementaryConfiguration"] = (
            aws_sdk_config_service.types.supplementary_configuration.serialize_aws_json_1_1(
                value["supplementary_configuration"]
            )
        )
    if "recording_frequency" in value:
        import aws_sdk_config_service.types.recording_frequency

        out["recordingFrequency"] = (
            aws_sdk_config_service.types.recording_frequency.serialize_aws_json_1_1(
                value["recording_frequency"]
            )
        )
    if "configuration_item_delivery_time" in value:
        import aws_sdk_config_service.types.configuration_item_delivery_time

        out["configurationItemDeliveryTime"] = (
            aws_sdk_config_service.types.configuration_item_delivery_time.serialize_aws_json_1_1(
                value["configuration_item_delivery_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfigurationItem:
    out: ConfigurationItem = {}  # type: ignore[typeddict-item]
    if "version" in data:
        out["version"] = data["version"]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "configurationItemCaptureTime" in data:
        import aws_sdk_config_service.types.configuration_item_capture_time

        out["configuration_item_capture_time"] = (
            aws_sdk_config_service.types.configuration_item_capture_time.deserialize_aws_json_1_1(
                data["configurationItemCaptureTime"]
            )
        )
    if "configurationItemStatus" in data:
        import aws_sdk_config_service.types.configuration_item_status

        out["configuration_item_status"] = (
            aws_sdk_config_service.types.configuration_item_status.deserialize_aws_json_1_1(
                data["configurationItemStatus"]
            )
        )
    if "configurationStateId" in data:
        out["configuration_state_id"] = data["configurationStateId"]
    if "configurationItemMD5Hash" in data:
        out["configuration_item_md5_hash"] = data["configurationItemMD5Hash"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "resourceType" in data:
        import aws_sdk_config_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_config_service.types.resource_type.deserialize_aws_json_1_1(
                data["resourceType"]
            )
        )
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "resourceName" in data:
        out["resource_name"] = data["resourceName"]
    if "awsRegion" in data:
        out["aws_region"] = data["awsRegion"]
    if "availabilityZone" in data:
        out["availability_zone"] = data["availabilityZone"]
    if "resourceCreationTime" in data:
        import aws_sdk_config_service.types.resource_creation_time

        out["resource_creation_time"] = (
            aws_sdk_config_service.types.resource_creation_time.deserialize_aws_json_1_1(
                data["resourceCreationTime"]
            )
        )
    if "tags" in data:
        import aws_sdk_config_service.types.tags

        out["tags"] = aws_sdk_config_service.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    if "relatedEvents" in data:
        import aws_sdk_config_service.types.related_event_list

        out["related_events"] = (
            aws_sdk_config_service.types.related_event_list.deserialize_aws_json_1_1(
                data["relatedEvents"]
            )
        )
    if "relationships" in data:
        import aws_sdk_config_service.types.relationship_list

        out["relationships"] = (
            aws_sdk_config_service.types.relationship_list.deserialize_aws_json_1_1(
                data["relationships"]
            )
        )
    if "configuration" in data:
        out["configuration"] = data["configuration"]
    if "supplementaryConfiguration" in data:
        import aws_sdk_config_service.types.supplementary_configuration

        out["supplementary_configuration"] = (
            aws_sdk_config_service.types.supplementary_configuration.deserialize_aws_json_1_1(
                data["supplementaryConfiguration"]
            )
        )
    if "recordingFrequency" in data:
        import aws_sdk_config_service.types.recording_frequency

        out["recording_frequency"] = (
            aws_sdk_config_service.types.recording_frequency.deserialize_aws_json_1_1(
                data["recordingFrequency"]
            )
        )
    if "configurationItemDeliveryTime" in data:
        import aws_sdk_config_service.types.configuration_item_delivery_time

        out["configuration_item_delivery_time"] = (
            aws_sdk_config_service.types.configuration_item_delivery_time.deserialize_aws_json_1_1(
                data["configurationItemDeliveryTime"]
            )
        )
    return out
