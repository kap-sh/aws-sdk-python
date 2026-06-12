"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#NeptuneSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.boolean_optional
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.string


class NeptuneSettings(TypedDict):
    service_access_role_arn: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint. The role must allow the <code>iam:PassRole</code> action. For more information, see <a href=\"https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole\">Creating an IAM Service Role for Accessing Amazon Neptune as a Target</a> in the <i>Database Migration Service User Guide. </i> </p>"""
    s3_bucket_name: "aws_sdk_database_migration_service.types.string.String"
    """<p>The name of the Amazon S3 bucket where DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. DMS maps the SQL source data to graph data before storing it in these .csv files.</p>"""
    s3_bucket_folder: "aws_sdk_database_migration_service.types.string.String"
    """<p>A folder path where you want DMS to store migrated graph data in the S3 bucket specified by <code>S3BucketName</code> </p>"""
    error_retry_duration: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of milliseconds for DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.</p>"""
    max_file_size: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The maximum size in kilobytes of migrated graph data stored in a .csv file before DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, DMS clears the bucket, ready to store the next batch of migrated graph data.</p>"""
    max_retry_count: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of times for DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error. The default is 5.</p>"""
    iam_auth_enabled: NotRequired[
        "aws_sdk_database_migration_service.types.boolean_optional.BooleanOptional"
    ]
    """<p>If you want Identity and Access Management (IAM) authorization enabled for this endpoint, set this parameter to <code>true</code>. Then attach the appropriate IAM policy document to your service role specified by <code>ServiceAccessRoleArn</code>. The default is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NeptuneSettings) -> dict:
    out: dict = {}
    if "service_access_role_arn" in value:
        out["ServiceAccessRoleArn"] = value["service_access_role_arn"]
    out["S3BucketName"] = value["s3_bucket_name"]
    out["S3BucketFolder"] = value["s3_bucket_folder"]
    if "error_retry_duration" in value:
        out["ErrorRetryDuration"] = value["error_retry_duration"]
    if "max_file_size" in value:
        out["MaxFileSize"] = value["max_file_size"]
    if "max_retry_count" in value:
        out["MaxRetryCount"] = value["max_retry_count"]
    if "iam_auth_enabled" in value:
        out["IamAuthEnabled"] = value["iam_auth_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NeptuneSettings:
    out: NeptuneSettings = {}  # type: ignore[typeddict-item]
    if "ServiceAccessRoleArn" in data:
        out["service_access_role_arn"] = data["ServiceAccessRoleArn"]
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        raise DeserializationError("NeptuneSettings.s3_bucket_name required")
    if "S3BucketFolder" in data:
        out["s3_bucket_folder"] = data["S3BucketFolder"]
    else:
        raise DeserializationError("NeptuneSettings.s3_bucket_folder required")
    if "ErrorRetryDuration" in data:
        out["error_retry_duration"] = data["ErrorRetryDuration"]
    if "MaxFileSize" in data:
        out["max_file_size"] = data["MaxFileSize"]
    if "MaxRetryCount" in data:
        out["max_retry_count"] = data["MaxRetryCount"]
    if "IamAuthEnabled" in data:
        out["iam_auth_enabled"] = data["IamAuthEnabled"]
    return out
