"""Generated from Smithy shape ``com.amazonaws.ec2#GetCapacityManagerAttributesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_manager_status
    import capo_ec2.types.ingestion_status
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class GetCapacityManagerAttributesResult(TypedDict, closed=True):
    capacity_manager_status: NotRequired[
        "capo_ec2.types.capacity_manager_status.CapacityManagerStatus"
    ]
    """<p> The current status of Capacity Manager. </p>"""
    organizations_access: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> Indicates whether Organizations access is enabled for cross-account data aggregation. </p>"""
    data_export_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p> The number of active data export configurations for this account. This count includes all data exports regardless of their current delivery status. </p>"""
    ingestion_status: NotRequired["capo_ec2.types.ingestion_status.IngestionStatus"]
    """<p> The current data ingestion status. Initial ingestion may take several hours after enabling Capacity Manager. </p>"""
    ingestion_status_message: NotRequired["capo_ec2.types.string.String"]
    """<p> A descriptive message providing additional details about the current ingestion status. This may include error information if ingestion has failed or progress details during initial setup. </p>"""
    earliest_datapoint_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp of the earliest data point available in Capacity Manager, in milliseconds since epoch. This indicates how far back historical data is available for queries. </p>"""
    latest_datapoint_timestamp: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp of the most recent data point ingested by Capacity Manager, in milliseconds since epoch. This indicates how current your capacity data is. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetCapacityManagerAttributesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_manager_status" in value:
        import capo_ec2.types.capacity_manager_status

        capo_ec2.types.capacity_manager_status.serialize_ec2_query(
            value["capacity_manager_status"],
            pairs,
            f"{key_prefix}CapacityManagerStatus",
        )
    if "organizations_access" in value:
        pairs.append(
            (
                f"{key_prefix}OrganizationsAccess",
                "true" if value["organizations_access"] else "false",
            )
        )
    if "data_export_count" in value:
        pairs.append((f"{key_prefix}DataExportCount", str(value["data_export_count"])))
    if "ingestion_status" in value:
        import capo_ec2.types.ingestion_status

        capo_ec2.types.ingestion_status.serialize_ec2_query(
            value["ingestion_status"], pairs, f"{key_prefix}IngestionStatus"
        )
    if "ingestion_status_message" in value:
        pairs.append(
            (
                f"{key_prefix}IngestionStatusMessage",
                str(value["ingestion_status_message"]),
            )
        )
    if "earliest_datapoint_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["earliest_datapoint_timestamp"],
            pairs,
            f"{key_prefix}EarliestDatapointTimestamp",
        )
    if "latest_datapoint_timestamp" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["latest_datapoint_timestamp"],
            pairs,
            f"{key_prefix}LatestDatapointTimestamp",
        )


def deserialize_ec2_query(el: Element) -> GetCapacityManagerAttributesResult:
    out: GetCapacityManagerAttributesResult = {}  # type: ignore[typeddict-item]
    child_capacity_manager_status = el.find("capacityManagerStatus")
    if child_capacity_manager_status is not None:
        import capo_ec2.types.capacity_manager_status

        out["capacity_manager_status"] = (
            capo_ec2.types.capacity_manager_status.deserialize_ec2_query(
                child_capacity_manager_status
            )
        )
    child_organizations_access = el.find("organizationsAccess")
    if child_organizations_access is not None:
        out["organizations_access"] = (
            child_organizations_access.text or ""
        ).lower() == "true"
    child_data_export_count = el.find("dataExportCount")
    if child_data_export_count is not None:
        out["data_export_count"] = int(child_data_export_count.text or "")
    child_ingestion_status = el.find("ingestionStatus")
    if child_ingestion_status is not None:
        import capo_ec2.types.ingestion_status

        out["ingestion_status"] = capo_ec2.types.ingestion_status.deserialize_ec2_query(
            child_ingestion_status
        )
    child_ingestion_status_message = el.find("ingestionStatusMessage")
    if child_ingestion_status_message is not None:
        out["ingestion_status_message"] = str(child_ingestion_status_message.text or "")
    child_earliest_datapoint_timestamp = el.find("earliestDatapointTimestamp")
    if child_earliest_datapoint_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["earliest_datapoint_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_earliest_datapoint_timestamp
            )
        )
    child_latest_datapoint_timestamp = el.find("latestDatapointTimestamp")
    if child_latest_datapoint_timestamp is not None:
        import capo_ec2.types.millisecond_date_time

        out["latest_datapoint_timestamp"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_latest_datapoint_timestamp
            )
        )
    return out
