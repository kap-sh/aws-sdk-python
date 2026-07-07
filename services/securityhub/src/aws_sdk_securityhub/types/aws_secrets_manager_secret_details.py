"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSecretsManagerSecretDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_secrets_manager_secret_rotation_rules
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsSecretsManagerSecretDetails(TypedDict, closed=True):
    rotation_rules: NotRequired[
        "aws_sdk_securityhub.types.aws_secrets_manager_secret_rotation_rules.AwsSecretsManagerSecretRotationRules"
    ]
    """<p>Defines the rotation schedule for the secret.</p>"""
    rotation_occurred_within_frequency: NotRequired[
        "aws_sdk_securityhub.types.boolean.Boolean"
    ]
    """<p>Whether the rotation occurred within the specified rotation frequency.</p>"""
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN, Key ID, or alias of the KMS key used to encrypt the <code>SecretString</code> or <code>SecretBinary</code> values for versions of this secret.</p>"""
    rotation_enabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether rotation is enabled.</p>"""
    rotation_lambda_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the Lambda function that rotates the secret.</p>"""
    deleted: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the secret is deleted.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the secret.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The user-provided description of the secret.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSecretsManagerSecretDetails) -> dict:
    out: dict = {}
    if "rotation_rules" in value:
        import aws_sdk_securityhub.types.aws_secrets_manager_secret_rotation_rules

        out["RotationRules"] = (
            aws_sdk_securityhub.types.aws_secrets_manager_secret_rotation_rules.serialize_json(
                value["rotation_rules"]
            )
        )
    if "rotation_occurred_within_frequency" in value:
        out["RotationOccurredWithinFrequency"] = value[
            "rotation_occurred_within_frequency"
        ]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "rotation_enabled" in value:
        out["RotationEnabled"] = value["rotation_enabled"]
    if "rotation_lambda_arn" in value:
        out["RotationLambdaArn"] = value["rotation_lambda_arn"]
    if "deleted" in value:
        out["Deleted"] = value["deleted"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> AwsSecretsManagerSecretDetails:
    out: AwsSecretsManagerSecretDetails = {}  # type: ignore[typeddict-item]
    if "RotationRules" in data:
        import aws_sdk_securityhub.types.aws_secrets_manager_secret_rotation_rules

        out["rotation_rules"] = (
            aws_sdk_securityhub.types.aws_secrets_manager_secret_rotation_rules.deserialize_json(
                data["RotationRules"]
            )
        )
    if "RotationOccurredWithinFrequency" in data:
        out["rotation_occurred_within_frequency"] = data[
            "RotationOccurredWithinFrequency"
        ]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "RotationEnabled" in data:
        out["rotation_enabled"] = data["RotationEnabled"]
    if "RotationLambdaArn" in data:
        out["rotation_lambda_arn"] = data["RotationLambdaArn"]
    if "Deleted" in data:
        out["deleted"] = data["Deleted"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
