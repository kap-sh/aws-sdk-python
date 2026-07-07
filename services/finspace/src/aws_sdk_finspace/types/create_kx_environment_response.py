"""Generated from Smithy shape ``com.amazonaws.finspace#CreateKxEnvironmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.description
    import aws_sdk_finspace.types.environment_arn
    import aws_sdk_finspace.types.environment_status
    import aws_sdk_finspace.types.id_type
    import aws_sdk_finspace.types.kms_key_id
    import aws_sdk_finspace.types.kx_environment_name
    import aws_sdk_finspace.types.timestamp


class CreateKxEnvironmentResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_finspace.types.kx_environment_name.KxEnvironmentName"]
    """<p>The name of the kdb environment.</p>"""
    status: NotRequired["aws_sdk_finspace.types.environment_status.EnvironmentStatus"]
    """<p>The status of the kdb environment.</p>"""
    environment_id: NotRequired["aws_sdk_finspace.types.id_type.IdType"]
    """<p>A unique identifier for the kdb environment.</p>"""
    description: NotRequired["aws_sdk_finspace.types.description.Description"]
    """<p>A description for the kdb environment.</p>"""
    environment_arn: NotRequired[
        "aws_sdk_finspace.types.environment_arn.EnvironmentArn"
    ]
    """<p>The ARN identifier of the environment.</p>"""
    kms_key_id: NotRequired["aws_sdk_finspace.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key ID to encrypt your data in the FinSpace environment.</p>"""
    creation_timestamp: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The timestamp at which the kdb environment was created in FinSpace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKxEnvironmentResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import aws_sdk_finspace.types.environment_status

        out["status"] = aws_sdk_finspace.types.environment_status.serialize_json(
            value["status"]
        )
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "environment_arn" in value:
        out["environmentArn"] = value["environment_arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "creation_timestamp" in value:
        import aws_sdk_finspace.types.timestamp

        out["creationTimestamp"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["creation_timestamp"]
        )
    return out


def deserialize_json(data: dict) -> CreateKxEnvironmentResponse:
    out: CreateKxEnvironmentResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_finspace.types.environment_status

        out["status"] = aws_sdk_finspace.types.environment_status.deserialize_json(
            data["status"]
        )
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "description" in data:
        out["description"] = data["description"]
    if "environmentArn" in data:
        out["environment_arn"] = data["environmentArn"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "creationTimestamp" in data:
        import aws_sdk_finspace.types.timestamp

        out["creation_timestamp"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["creationTimestamp"]
        )
    return out
