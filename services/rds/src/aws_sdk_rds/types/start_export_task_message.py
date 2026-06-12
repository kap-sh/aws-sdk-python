"""Generated from Smithy shape ``com.amazonaws.rds#StartExportTaskMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.string_list


class StartExportTaskMessage(TypedDict):
    export_task_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>A unique identifier for the export task. This ID isn't an identifier for the Amazon S3 bucket where the data is to be exported.</p>"""
    source_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot or cluster to export to Amazon S3.</p>"""
    s3_bucket_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the Amazon S3 bucket to export the snapshot or cluster data to.</p>"""
    iam_role_arn: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the IAM role to use for writing to the Amazon S3 bucket when exporting a snapshot or cluster.</p> <p>In the IAM policy attached to your IAM role, include the following required actions to allow the transfer of files from Amazon RDS or Amazon Aurora to an S3 bucket:</p> <ul> <li> <p>s3:PutObject*</p> </li> <li> <p>s3:GetObject*</p> </li> <li> <p>s3:ListBucket</p> </li> <li> <p>s3:DeleteObject*</p> </li> <li> <p>s3:GetBucketLocation </p> </li> </ul> <p>In the policy, include the resources to identify the S3 bucket and objects in the bucket. The following list of resources shows the Amazon Resource Name (ARN) format for accessing S3:</p> <ul> <li> <p> <code>arn:aws:s3:::<i>your-s3-bucket</i> </code> </p> </li> <li> <p> <code>arn:aws:s3:::<i>your-s3-bucket</i>/*</code> </p> </li> </ul>"""
    kms_key_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The ID of the Amazon Web Services KMS key to use to encrypt the data exported to Amazon S3. The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key. The caller of this operation must be authorized to run the following operations. These can be set in the Amazon Web Services KMS key policy:</p> <ul> <li> <p>kms:CreateGrant</p> </li> <li> <p>kms:DescribeKey</p> </li> </ul>"""
    s3_prefix: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon S3 bucket prefix to use as the file name and path of the exported data.</p>"""
    export_only: NotRequired["aws_sdk_rds.types.string_list.StringList"]
    """<p>The data to be exported from the snapshot or cluster. If this parameter isn't provided, all of the data is exported.</p> <p>Valid Values:</p> <ul> <li> <p> <code>database</code> - Export all the data from a specified database.</p> </li> <li> <p> <code>database.table</code> <i>table-name</i> - Export a table of the snapshot or cluster. This format is valid only for RDS for MySQL, RDS for MariaDB, and Aurora MySQL.</p> </li> <li> <p> <code>database.schema</code> <i>schema-name</i> - Export a database schema of the snapshot or cluster. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.</p> </li> <li> <p> <code>database.schema.table</code> <i>table-name</i> - Export a table of the database schema. This format is valid only for RDS for PostgreSQL and Aurora PostgreSQL.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StartExportTaskMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "export_task_identifier" in value:
        pairs.append(
            (f"{prefix}.ExportTaskIdentifier", str(value["export_task_identifier"]))
        )
    if "source_arn" in value:
        pairs.append((f"{prefix}.SourceArn", str(value["source_arn"])))
    if "s3_bucket_name" in value:
        pairs.append((f"{prefix}.S3BucketName", str(value["s3_bucket_name"])))
    if "iam_role_arn" in value:
        pairs.append((f"{prefix}.IamRoleArn", str(value["iam_role_arn"])))
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "s3_prefix" in value:
        pairs.append((f"{prefix}.S3Prefix", str(value["s3_prefix"])))
    if "export_only" in value:
        import aws_sdk_rds.types.string_list

        aws_sdk_rds.types.string_list.serialize_query(
            value["export_only"], pairs, f"{prefix}.ExportOnly"
        )


def deserialize_query(el: Element) -> StartExportTaskMessage:
    out: StartExportTaskMessage = {}  # type: ignore[typeddict-item]
    child_export_task_identifier = el.find("ExportTaskIdentifier")
    if child_export_task_identifier is not None:
        out["export_task_identifier"] = str(child_export_task_identifier.text or "")
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_s3_bucket_name = el.find("S3BucketName")
    if child_s3_bucket_name is not None:
        out["s3_bucket_name"] = str(child_s3_bucket_name.text or "")
    child_iam_role_arn = el.find("IamRoleArn")
    if child_iam_role_arn is not None:
        out["iam_role_arn"] = str(child_iam_role_arn.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_s3_prefix = el.find("S3Prefix")
    if child_s3_prefix is not None:
        out["s3_prefix"] = str(child_s3_prefix.text or "")
    child_export_only = el.find("ExportOnly")
    if child_export_only is not None:
        import aws_sdk_rds.types.string_list

        out["export_only"] = aws_sdk_rds.types.string_list.deserialize_query(
            child_export_only
        )
    return out
