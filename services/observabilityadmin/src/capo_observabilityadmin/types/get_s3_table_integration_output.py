"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetS3TableIntegrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.encryption
    import capo_observabilityadmin.types.integration_status
    import capo_observabilityadmin.types.resource_arn


class GetS3TableIntegrationOutput(TypedDict, closed=True):
    arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the S3 Table integration.</p>"""
    role_arn: NotRequired["capo_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role used by the S3 Table integration.</p>"""
    status: NotRequired[
        "capo_observabilityadmin.types.integration_status.IntegrationStatus"
    ]
    """<p>The current status of the S3 Table integration.</p>"""
    encryption: NotRequired["capo_observabilityadmin.types.encryption.Encryption"]
    """<p>The encryption configuration for the S3 Table integration.</p>"""
    destination_table_bucket_arn: NotRequired[
        "capo_observabilityadmin.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the S3 bucket used as the destination for the table data.</p>"""
    created_time_stamp: NotRequired["int"]
    """<p>The timestamp when the S3 Table integration was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetS3TableIntegrationOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "status" in value:
        import capo_observabilityadmin.types.integration_status

        out["Status"] = capo_observabilityadmin.types.integration_status.serialize_json(
            value["status"]
        )
    if "encryption" in value:
        import capo_observabilityadmin.types.encryption

        out["Encryption"] = capo_observabilityadmin.types.encryption.serialize_json(
            value["encryption"]
        )
    if "destination_table_bucket_arn" in value:
        out["DestinationTableBucketArn"] = value["destination_table_bucket_arn"]
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    return out


def deserialize_json(data: dict) -> GetS3TableIntegrationOutput:
    out: GetS3TableIntegrationOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Status" in data:
        import capo_observabilityadmin.types.integration_status

        out["status"] = (
            capo_observabilityadmin.types.integration_status.deserialize_json(
                data["Status"]
            )
        )
    if "Encryption" in data:
        import capo_observabilityadmin.types.encryption

        out["encryption"] = capo_observabilityadmin.types.encryption.deserialize_json(
            data["Encryption"]
        )
    if "DestinationTableBucketArn" in data:
        out["destination_table_bucket_arn"] = data["DestinationTableBucketArn"]
    if "CreatedTimeStamp" in data:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    return out
