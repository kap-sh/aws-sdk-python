"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerDataExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.capacity_manager_data_export_id
    import capo_ec2.types.capacity_manager_data_export_status
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.output_format
    import capo_ec2.types.schedule
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class CapacityManagerDataExportResponse(TypedDict, closed=True):
    capacity_manager_data_export_id: NotRequired[
        "capo_ec2.types.capacity_manager_data_export_id.CapacityManagerDataExportId"
    ]
    """<p> The unique identifier for the data export configuration. </p>"""
    s3_bucket_name: NotRequired["capo_ec2.types.string.String"]
    """<p> The name of the S3 bucket where export files are delivered. </p>"""
    s3_bucket_prefix: NotRequired["capo_ec2.types.string.String"]
    """<p> The S3 key prefix used for organizing export files within the bucket. </p>"""
    schedule: NotRequired["capo_ec2.types.schedule.Schedule"]
    """<p> The frequency at which data exports are generated. </p>"""
    output_format: NotRequired["capo_ec2.types.output_format.OutputFormat"]
    """<p> The file format of the exported data. </p>"""
    create_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p> The timestamp when the data export configuration was created. </p>"""
    latest_delivery_status: NotRequired[
        "capo_ec2.types.capacity_manager_data_export_status.CapacityManagerDataExportStatus"
    ]
    """<p> The status of the most recent export delivery. </p>"""
    latest_delivery_status_message: NotRequired["capo_ec2.types.string.String"]
    """<p> A message describing the status of the most recent export delivery, including any error details if the delivery failed. </p>"""
    latest_delivery_s3_location_uri: NotRequired["capo_ec2.types.string.String"]
    """<p> The S3 URI of the most recently delivered export file. </p>"""
    latest_delivery_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p> The timestamp when the most recent export was delivered to S3. </p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p> The tags associated with the data export configuration. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerDataExportResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_manager_data_export_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityManagerDataExportId",
                str(value["capacity_manager_data_export_id"]),
            )
        )
    if "s3_bucket_name" in value:
        pairs.append((f"{key_prefix}S3BucketName", str(value["s3_bucket_name"])))
    if "s3_bucket_prefix" in value:
        pairs.append((f"{key_prefix}S3BucketPrefix", str(value["s3_bucket_prefix"])))
    if "schedule" in value:
        import capo_ec2.types.schedule

        capo_ec2.types.schedule.serialize_ec2_query(
            value["schedule"], pairs, f"{key_prefix}Schedule"
        )
    if "output_format" in value:
        import capo_ec2.types.output_format

        capo_ec2.types.output_format.serialize_ec2_query(
            value["output_format"], pairs, f"{key_prefix}OutputFormat"
        )
    if "create_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "latest_delivery_status" in value:
        import capo_ec2.types.capacity_manager_data_export_status

        capo_ec2.types.capacity_manager_data_export_status.serialize_ec2_query(
            value["latest_delivery_status"], pairs, f"{key_prefix}LatestDeliveryStatus"
        )
    if "latest_delivery_status_message" in value:
        pairs.append(
            (
                f"{key_prefix}LatestDeliveryStatusMessage",
                str(value["latest_delivery_status_message"]),
            )
        )
    if "latest_delivery_s3_location_uri" in value:
        pairs.append(
            (
                f"{key_prefix}LatestDeliveryS3LocationUri",
                str(value["latest_delivery_s3_location_uri"]),
            )
        )
    if "latest_delivery_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["latest_delivery_time"], pairs, f"{key_prefix}LatestDeliveryTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )


def deserialize_ec2_query(el: Element) -> CapacityManagerDataExportResponse:
    out: CapacityManagerDataExportResponse = {}  # type: ignore[typeddict-item]
    child_capacity_manager_data_export_id = el.find("capacityManagerDataExportId")
    if child_capacity_manager_data_export_id is not None:
        out["capacity_manager_data_export_id"] = str(
            child_capacity_manager_data_export_id.text or ""
        )
    child_s3_bucket_name = el.find("s3BucketName")
    if child_s3_bucket_name is not None:
        out["s3_bucket_name"] = str(child_s3_bucket_name.text or "")
    child_s3_bucket_prefix = el.find("s3BucketPrefix")
    if child_s3_bucket_prefix is not None:
        out["s3_bucket_prefix"] = str(child_s3_bucket_prefix.text or "")
    child_schedule = el.find("schedule")
    if child_schedule is not None:
        import capo_ec2.types.schedule

        out["schedule"] = capo_ec2.types.schedule.deserialize_ec2_query(child_schedule)
    child_output_format = el.find("outputFormat")
    if child_output_format is not None:
        import capo_ec2.types.output_format

        out["output_format"] = capo_ec2.types.output_format.deserialize_ec2_query(
            child_output_format
        )
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["create_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_create_time
        )
    child_latest_delivery_status = el.find("latestDeliveryStatus")
    if child_latest_delivery_status is not None:
        import capo_ec2.types.capacity_manager_data_export_status

        out["latest_delivery_status"] = (
            capo_ec2.types.capacity_manager_data_export_status.deserialize_ec2_query(
                child_latest_delivery_status
            )
        )
    child_latest_delivery_status_message = el.find("latestDeliveryStatusMessage")
    if child_latest_delivery_status_message is not None:
        out["latest_delivery_status_message"] = str(
            child_latest_delivery_status_message.text or ""
        )
    child_latest_delivery_s3_location_uri = el.find("latestDeliveryS3LocationUri")
    if child_latest_delivery_s3_location_uri is not None:
        out["latest_delivery_s3_location_uri"] = str(
            child_latest_delivery_s3_location_uri.text or ""
        )
    child_latest_delivery_time = el.find("latestDeliveryTime")
    if child_latest_delivery_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["latest_delivery_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_latest_delivery_time
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    return out
