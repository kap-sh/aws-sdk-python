"""Generated from Smithy shape ``com.amazonaws.secretsmanager#DeleteSecretResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.deletion_date_type
    import aws_sdk_secrets_manager.types.secret_arn_type
    import aws_sdk_secrets_manager.types.secret_name_type


class DeleteSecretResponse(TypedDict):
    arn: NotRequired["aws_sdk_secrets_manager.types.secret_arn_type.SecretARNType"]
    """<p>The ARN of the secret.</p>"""
    name: NotRequired["aws_sdk_secrets_manager.types.secret_name_type.SecretNameType"]
    """<p>The name of the secret.</p>"""
    deletion_date: NotRequired[
        "aws_sdk_secrets_manager.types.deletion_date_type.DeletionDateType"
    ]
    """<p>The date and time after which this secret Secrets Manager can permanently delete this secret, and it can no longer be restored. This value is the date and time of the delete request plus the number of days in <code>RecoveryWindowInDays</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSecretResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["ARN"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "deletion_date" in value:
        import aws_sdk_secrets_manager.types.deletion_date_type

        out["DeletionDate"] = (
            aws_sdk_secrets_manager.types.deletion_date_type.serialize_aws_json_1_1(
                value["deletion_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSecretResponse:
    out: DeleteSecretResponse = {}  # type: ignore[typeddict-item]
    if "ARN" in data:
        out["arn"] = data["ARN"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DeletionDate" in data:
        import aws_sdk_secrets_manager.types.deletion_date_type

        out["deletion_date"] = (
            aws_sdk_secrets_manager.types.deletion_date_type.deserialize_aws_json_1_1(
                data["DeletionDate"]
            )
        )
    return out
