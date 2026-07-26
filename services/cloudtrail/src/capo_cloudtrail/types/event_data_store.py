"""Generated from Smithy shape ``com.amazonaws.cloudtrail#EventDataStore``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.advanced_event_selectors
    import capo_cloudtrail.types.boolean
    import capo_cloudtrail.types.date
    import capo_cloudtrail.types.event_data_store_arn
    import capo_cloudtrail.types.event_data_store_name
    import capo_cloudtrail.types.event_data_store_status
    import capo_cloudtrail.types.retention_period
    import capo_cloudtrail.types.termination_protection_enabled


class EventDataStore(TypedDict, closed=True):
    event_data_store_arn: NotRequired[
        "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    ]
    """<p>The ARN of the event data store.</p>"""
    name: NotRequired["capo_cloudtrail.types.event_data_store_name.EventDataStoreName"]
    """<p>The name of the event data store.</p>"""
    termination_protection_enabled: NotRequired[
        "capo_cloudtrail.types.termination_protection_enabled.TerminationProtectionEnabled"
    ]
    """<p>Indicates whether the event data store is protected from termination.</p>"""
    status: NotRequired[
        "capo_cloudtrail.types.event_data_store_status.EventDataStoreStatus"
    ]
    """<p>The status of an event data store.</p>"""
    advanced_event_selectors: NotRequired[
        "capo_cloudtrail.types.advanced_event_selectors.AdvancedEventSelectors"
    ]
    """<p>The advanced event selectors that were used to select events for the data store.</p>"""
    multi_region_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Indicates whether the event data store includes events from all Regions, or only from the Region in which it was created.</p>"""
    organization_enabled: NotRequired["capo_cloudtrail.types.boolean.Boolean"]
    """<p>Indicates that an event data store is collecting logged events for an organization.</p>"""
    retention_period: NotRequired[
        "capo_cloudtrail.types.retention_period.RetentionPeriod"
    ]
    """<p>The retention period, in days.</p>"""
    created_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The timestamp of the event data store's creation.</p>"""
    updated_timestamp: NotRequired["capo_cloudtrail.types.date.Date"]
    """<p>The timestamp showing when an event data store was updated, if applicable. <code>UpdatedTimestamp</code> is always either the same or newer than the time shown in <code>CreatedTimestamp</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventDataStore) -> dict:
    out: dict = {}
    if "event_data_store_arn" in value:
        out["EventDataStoreArn"] = value["event_data_store_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "termination_protection_enabled" in value:
        out["TerminationProtectionEnabled"] = value["termination_protection_enabled"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> EventDataStore:
    out: EventDataStore = {}  # type: ignore[typeddict-item]
    if "EventDataStoreArn" in data:
        out["event_data_store_arn"] = data["EventDataStoreArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "TerminationProtectionEnabled" in data:
        out["termination_protection_enabled"] = data["TerminationProtectionEnabled"]
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
    return out
