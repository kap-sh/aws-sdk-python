"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityManagerDataExportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.output_format
    import aws_sdk_ec2.types.schedule
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CreateCapacityManagerDataExportRequest(TypedDict):
    s3_bucket_name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The name of the S3 bucket where the capacity data export files will be delivered. The bucket must exist and you must have write permissions to it. </p>"""
    s3_bucket_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> The S3 key prefix for the exported data files. This allows you to organize exports in a specific folder structure within your bucket. If not specified, files are placed at the bucket root. </p>"""
    schedule: NotRequired["aws_sdk_ec2.types.schedule.Schedule"]
    """<p> The frequency at which data exports are generated. </p>"""
    output_format: NotRequired["aws_sdk_ec2.types.output_format.OutputFormat"]
    """<p> The file format for the exported data. Parquet format is recommended for large datasets and better compression. </p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p> Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see Ensure Idempotency. </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p> Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>. </p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p> The tags to apply to the data export configuration. You can tag the export for organization and cost tracking purposes. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityManagerDataExportRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "s3_bucket_name" in value:
        pairs.append((f"{prefix}.S3BucketName", str(value["s3_bucket_name"])))
    if "s3_bucket_prefix" in value:
        pairs.append((f"{prefix}.S3BucketPrefix", str(value["s3_bucket_prefix"])))
    if "schedule" in value:
        import aws_sdk_ec2.types.schedule

        aws_sdk_ec2.types.schedule.serialize_ec2_query(
            value["schedule"], pairs, f"{prefix}.Schedule"
        )
    if "output_format" in value:
        import aws_sdk_ec2.types.output_format

        aws_sdk_ec2.types.output_format.serialize_ec2_query(
            value["output_format"], pairs, f"{prefix}.OutputFormat"
        )
    if "client_token" in value:
        pairs.append((f"{prefix}.ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import aws_sdk_ec2.types.tag_specification_list

        aws_sdk_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{prefix}.TagSpecifications"
        )


def deserialize_ec2_query(el: Element) -> CreateCapacityManagerDataExportRequest:
    out: CreateCapacityManagerDataExportRequest = {}  # type: ignore[typeddict-item]
    child_s3_bucket_name = el.find("S3BucketName")
    if child_s3_bucket_name is not None:
        out["s3_bucket_name"] = str(child_s3_bucket_name.text or "")
    child_s3_bucket_prefix = el.find("S3BucketPrefix")
    if child_s3_bucket_prefix is not None:
        out["s3_bucket_prefix"] = str(child_s3_bucket_prefix.text or "")
    child_schedule = el.find("Schedule")
    if child_schedule is not None:
        import aws_sdk_ec2.types.schedule

        out["schedule"] = aws_sdk_ec2.types.schedule.deserialize_ec2_query(
            child_schedule
        )
    child_output_format = el.find("OutputFormat")
    if child_output_format is not None:
        import aws_sdk_ec2.types.output_format

        out["output_format"] = aws_sdk_ec2.types.output_format.deserialize_ec2_query(
            child_output_format
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    if el.find("TagSpecifications") is not None:
        import aws_sdk_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            aws_sdk_ec2.types.tag_specification_list.deserialize_ec2_query(
                el, "TagSpecifications"
            )
        )
    return out
