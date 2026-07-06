"""Generated from Smithy shape ``com.amazonaws.workmail#StartMailboxExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.description
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.idempotency_client_token
    import aws_sdk_workmail.types.kms_key_arn
    import aws_sdk_workmail.types.organization_id
    import aws_sdk_workmail.types.role_arn
    import aws_sdk_workmail.types.s3_bucket_name
    import aws_sdk_workmail.types.s3_object_key


class StartMailboxExportJobRequest(TypedDict, closed=True):
    client_token: (
        "aws_sdk_workmail.types.idempotency_client_token.IdempotencyClientToken"
    )
    """<p>The idempotency token for the client request.</p>"""
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier associated with the organization.</p>"""
    entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the user or resource associated with the mailbox.</p> <p>The identifier can accept <i>UserId or ResourceId</i>, <i>Username or Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789 , or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>"""
    description: NotRequired["aws_sdk_workmail.types.description.Description"]
    """<p>The mailbox export job description.</p>"""
    role_arn: "aws_sdk_workmail.types.role_arn.RoleArn"
    """<p>The ARN of the AWS Identity and Access Management (IAM) role that grants write permission to the S3 bucket.</p>"""
    kms_key_arn: "aws_sdk_workmail.types.kms_key_arn.KmsKeyArn"
    """<p>The Amazon Resource Name (ARN) of the symmetric AWS Key Management Service (AWS KMS) key that encrypts the exported mailbox content.</p>"""
    s3_bucket_name: "aws_sdk_workmail.types.s3_bucket_name.S3BucketName"
    """<p>The name of the S3 bucket.</p>"""
    s3_prefix: "aws_sdk_workmail.types.s3_object_key.S3ObjectKey"
    """<p>The S3 bucket prefix.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMailboxExportJobRequest) -> dict:
    out: dict = {}
    out["ClientToken"] = value["client_token"]
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    if "description" in value:
        out["Description"] = value["description"]
    out["RoleArn"] = value["role_arn"]
    out["KmsKeyArn"] = value["kms_key_arn"]
    out["S3BucketName"] = value["s3_bucket_name"]
    out["S3Prefix"] = value["s3_prefix"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMailboxExportJobRequest:
    out: StartMailboxExportJobRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("StartMailboxExportJobRequest.client_token required")
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "StartMailboxExportJobRequest.organization_id required"
        )
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("StartMailboxExportJobRequest.entity_id required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("StartMailboxExportJobRequest.role_arn required")
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    else:
        raise DeserializationError("StartMailboxExportJobRequest.kms_key_arn required")
    if "S3BucketName" in data:
        out["s3_bucket_name"] = data["S3BucketName"]
    else:
        raise DeserializationError(
            "StartMailboxExportJobRequest.s3_bucket_name required"
        )
    if "S3Prefix" in data:
        out["s3_prefix"] = data["S3Prefix"]
    else:
        raise DeserializationError("StartMailboxExportJobRequest.s3_prefix required")
    return out
