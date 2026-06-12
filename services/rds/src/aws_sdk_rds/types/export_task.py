"""Generated from Smithy shape ``com.amazonaws.rds#ExportTask``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.export_source_type
    import aws_sdk_rds.types.integer
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.string_list
    import aws_sdk_rds.types.t_stamp


class ExportTask(TypedDict):
    export_task_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A unique identifier for the snapshot or cluster export task. This ID isn't an identifier for the Amazon S3 bucket where the data is exported.</p>"""
    source_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.</p>"""
    export_only: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>The data exported from the snapshot or cluster.</p> <p>Valid Values:</p> <ul> <li> <p> <code>database</code> - Export all the data from a specified database.</p> </li> <li> <p> <code>database.table</code> <i>table-name</i> - Export a table of the snapshot or cluster. This format is valid only for RDS for MySQL, RDS for MariaDB, and Aurora MySQL.</p> </li> <li> <p> <code>database.schema</code> <i>schema-name</i> - Export a database schema of the snapshot or cluster. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.</p> </li> <li> <p> <code>database.schema.table</code> <i>table-name</i> - Export a table of the database schema. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.</p> </li> </ul>"""
    snapshot_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The time when the snapshot was created.</p>"""
    task_start_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The time when the snapshot or cluster export task started.</p>"""
    task_end_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The time when the snapshot or cluster export task ended.</p>"""
    s3_bucket: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon S3 bucket where the snapshot or cluster is exported to.</p>"""
    s3_prefix: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon S3 bucket prefix that is the file name and path of the exported data.</p>"""
    iam_role_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the IAM role that is used to write to Amazon S3 when exporting a snapshot or cluster.</p>"""
    kms_key_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The key identifier of the Amazon Web Services KMS key that is used to encrypt the data when it's exported to Amazon S3. The KMS key identifier is its key ARN, key ID, alias ARN, or alias name. The IAM role used for the export must have encryption and decryption permissions to use this KMS key.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The progress status of the export task. The status can be one of the following:</p> <ul> <li> <p> <code>CANCELED</code> </p> </li> <li> <p> <code>CANCELING</code> </p> </li> <li> <p> <code>COMPLETE</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>IN_PROGRESS</code> </p> </li> <li> <p> <code>STARTING</code> </p> </li> </ul>"""
    percent_progress: NotRequired["aws_sdk_rds.types.integer.Integer"]
    """<p>The progress of the snapshot or cluster export task as a percentage.</p>"""
    total_extracted_data_in_gb: NotRequired["aws_sdk_rds.types.integer.Integer"]
    """<p>The total amount of data exported, in gigabytes.</p>"""
    failure_cause: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The reason the export failed, if it failed.</p>"""
    warning_message: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A warning about the snapshot or cluster export task.</p>"""
    source_type: NotRequired["aws_sdk_rds.types.export_source_type.ExportSourceType"]
    """<p>The type of source for the export.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ExportTask, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "export_task_identifier" in value:
        pairs.append(
            (f"{prefix}.ExportTaskIdentifier", str(value["export_task_identifier"]))
        )
    if "source_arn" in value:
        pairs.append((f"{prefix}.SourceArn", str(value["source_arn"])))
    if "export_only" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["export_only"], pairs, f"{prefix}.ExportOnly"
        )
    if "snapshot_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["snapshot_time"], pairs, f"{prefix}.SnapshotTime"
        )
    if "task_start_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["task_start_time"], pairs, f"{prefix}.TaskStartTime"
        )
    if "task_end_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["task_end_time"], pairs, f"{prefix}.TaskEndTime"
        )
    if "s3_bucket" in value:
        pairs.append((f"{prefix}.S3Bucket", str(value["s3_bucket"])))
    if "s3_prefix" in value:
        pairs.append((f"{prefix}.S3Prefix", str(value["s3_prefix"])))
    if "iam_role_arn" in value:
        pairs.append((f"{prefix}.IamRoleArn", str(value["iam_role_arn"])))
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))
    if "percent_progress" in value:
        pairs.append((f"{prefix}.PercentProgress", str(value["percent_progress"])))
    if "total_extracted_data_in_gb" in value:
        pairs.append(
            (
                f"{prefix}.TotalExtractedDataInGB",
                str(value["total_extracted_data_in_gb"]),
            )
        )
    if "failure_cause" in value:
        pairs.append((f"{prefix}.FailureCause", str(value["failure_cause"])))
    if "warning_message" in value:
        pairs.append((f"{prefix}.WarningMessage", str(value["warning_message"])))
    if "source_type" in value:
        import aws_sdk_rds.types.export_source_type

        aws_sdk_rds.types.export_source_type.serialize_query(
            value["source_type"], pairs, f"{prefix}.SourceType"
        )


def deserialize_query(el: Element) -> ExportTask:
    out: ExportTask = {}  # type: ignore[typeddict-item]
    child_export_task_identifier = el.find("ExportTaskIdentifier")
    if child_export_task_identifier is not None:
        out["export_task_identifier"] = str(child_export_task_identifier.text or "")
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_export_only = el.find("ExportOnly")
    if child_export_only is not None:
        import aws_sdk_rds.types.string_list

        out["export_only"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_export_only
        )
    child_snapshot_time = el.find("SnapshotTime")
    if child_snapshot_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["snapshot_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_snapshot_time
        )
    child_task_start_time = el.find("TaskStartTime")
    if child_task_start_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["task_start_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_task_start_time
        )
    child_task_end_time = el.find("TaskEndTime")
    if child_task_end_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["task_end_time"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_task_end_time
        )
    child_s3_bucket = el.find("S3Bucket")
    if child_s3_bucket is not None:
        out["s3_bucket"] = str(child_s3_bucket.text or "")
    child_s3_prefix = el.find("S3Prefix")
    if child_s3_prefix is not None:
        out["s3_prefix"] = str(child_s3_prefix.text or "")
    child_iam_role_arn = el.find("IamRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_percent_progress = el.find("PercentProgress")
    if child_percent_progress is not None:
        out["percent_progress"] = int(child_percent_progress.text or "")
    child_total_extracted_data_in_gb = el.find("TotalExtractedDataInGB")
    if child_total_extracted_data_in_gb is not None:
        out["total_extracted_data_in_gb"] = int(
            child_total_extracted_data_in_gb.text or ""
        )
    child_failure_cause = el.find("FailureCause")
    if child_failure_cause is not None:
        out["failure_cause"] = str(child_failure_cause.text or "")
    child_warning_message = el.find("WarningMessage")
    if child_warning_message is not None:
        out["warning_message"] = str(child_warning_message.text or "")
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import aws_sdk_rds.types.export_source_type

        out["source_type"] = aws_sdk_rds.types.export_source_type.deserialize_query(
            child_source_type
        )
    return out
