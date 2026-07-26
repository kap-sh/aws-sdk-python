"""Generated from Smithy shape ``com.amazonaws.cloudtrail#CreateEventDataStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_event_selectors
    import capo_cloudtrail.types.billing_mode
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.event_data_store_kms_key_id
    import capo_cloudtrail.types.event_data_store_name
    import capo_cloudtrail.types.event_data_store_status
    import capo_cloudtrail.types.retention_period
    import capo_cloudtrail.types.tags_list
    import capo_cloudtrail.types.termination_protection_enabled


class CreateEventDataStoreResponse(TypedDict, closed=True):
    event_data_store_arn: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN of the event data store.</p>"""
    name: NotRequired["capo_cloudtrail.types.event_data_store_name.EventDataStoreName"]
    """<p>The name of the event data store.</p>"""
    status: NotRequired[
        "capo_cloudtrail.types.event_data_store_status.EventDataStoreStatus"
    ]
    """<p>The status of event data store creation.</p>"""
    advanced_event_selectors: NotRequired[
        "capo_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p>The advanced event selectors that were used to select the events for the data store.</p>"""
    multi_region_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Indicates whether the event data store collects events from all Regions, or only from the Region in which it was created.</p>"""
    organization_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Indicates whether an event data store is collecting logged events for an organization in Organizations.</p>"""
    retention_period: NotRequired[
        "capo_cloudtrail.types.retention_period.RetentionPeriod"
    ]
    """<p>The retention period of an event data store, in days.</p>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p>Indicates whether termination protection is enabled for the event data store.</p>"""
    tags_list: NotRequired["capo_cloudtrail.types.tags_list.TagsList"]
    created_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The timestamp that shows when the event data store was created.</p>"""
    updated_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The timestamp that shows when an event data store was updated, if applicable. <code>UpdatedTimestamp</code> is always either the same or newer than the time shown in <code>CreatedTimestamp</code>.</p>"""
    kms_key_id: NotRequired[
        "capo_cloudtrail.types.event_data_store_kms_key_id.EventDataStoreKmsKeyId"
    ]
    """<p>Specifies the KMS key ID that encrypts the events delivered by CloudTrail. The value is a fully specified ARN to a KMS key in the following format.</p> <p> <code>arn:aws:kms:us-east-2:123456789012:key/12345678-1234-1234-1234-123456789012</code> </p>"""
    billing_mode: NotRequired["capo_cloudtrail.types.billing_mode.BillingMode"]
    """<p>The billing mode for the event data store.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEventDataStoreResponse) -> dict:
    out: dict = {}
    if "event_data_store_arn" in value:
        out["EventDataStoreArn"] = value["event_data_store_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_cloudtrail.types.event_data_store_status

        out["Status"] = (
            capo_cloudtrail.types.event_data_store_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "advanced_event_selectors" in value:
        import capo_cloudtrail.types.advanced_event_selectors

        out["AdvancedEventSelectors"] = (
            capo_cloudtrail.types.advanced_event_selectors.serialize_aws_json_1_1(
                value["advanced_event_selectors"]
            )
        )
    if "multi_region_enabled" in value:
        out["MultiRegionEnabled"] = value["multi_region_enabled"]
    if "organization_enabled" in value:
        out["OrganizationEnabled"] = value["organization_enabled"]
    if "retention_period" in value:
        out["RetentionPeriod"] = value["retention_period"]
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
    if "tags_list" in value:
        import capo_cloudtrail.types.tags_list

        out["TagsList"] = capo_cloudtrail.types.tags_list.serialize_aws_json_1_1(
            value["tags_list"]
        )
    if "created_timestamp" in value:
        import capo_cloudtrail.types.date

        out["CreatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["created_timestamp"]
        )
    if "updated_timestamp" in value:
        import capo_cloudtrail.types.date

        out["UpdatedTimestamp"] = capo_cloudtrail.types.date.serialize_aws_json_1_1(
            value["updated_timestamp"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "billing_mode" in value:
        import capo_cloudtrail.types.billing_mode

        out["BillingMode"] = capo_cloudtrail.types.billing_mode.serialize_aws_json_1_1(
            value["billing_mode"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEventDataStoreResponse:
    out: CreateEventDataStoreResponse = {}  # type: ignore[typeddict-item]
    if "EventDataStoreArn" in data:
        out["event_data_store_arn"] = data["EventDataStoreArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import capo_cloudtrail.types.event_data_store_status

        out["status"] = (
            capo_cloudtrail.types.event_data_store_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "AdvancedEventSelectors" in data:
        import capo_cloudtrail.types.advanced_event_selectors

        out["advanced_event_selectors"] = (
            capo_cloudtrail.types.advanced_event_selectors.deserialize_aws_json_1_1(
                data["AdvancedEventSelectors"]
            )
        )
    if "MultiRegionEnabled" in data:
        out["multi_region_enabled"] = data["MultiRegionEnabled"]
    if "OrganizationEnabled" in data:
        out["organization_enabled"] = data["OrganizationEnabled"]
    if "RetentionPeriod" in data:
        out["retention_period"] = data["RetentionPeriod"]
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
    if "TagsList" in data:
        import capo_cloudtrail.types.tags_list

        out["tags_list"] = capo_cloudtrail.types.tags_list.deserialize_aws_json_1_1(
            data["TagsList"]
        )
    if "CreatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["created_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["CreatedTimestamp"]
        )
    if "UpdatedTimestamp" in data:
        import capo_cloudtrail.types.date

        out["updated_timestamp"] = capo_cloudtrail.types.date.deserialize_aws_json_1_1(
            data["UpdatedTimestamp"]
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "BillingMode" in data:
        import capo_cloudtrail.types.billing_mode

        out["billing_mode"] = (
            capo_cloudtrail.types.billing_mode.deserialize_aws_json_1_1(
                data["BillingMode"]
            )
        )
    return out
