"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateS3TableIntegrationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.encryption
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.tag_map_input


class CreateS3TableIntegrationInput(TypedDict):
    encryption: "aws_sdk_observabilityadmin.types.encryption.Encryption"
    """<p>The encryption configuration for the S3 Table integration, including the encryption algorithm and KMS key settings.</p>"""
    role_arn: "aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.</p>"""
    tags: NotRequired["aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p>The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateS3TableIntegrationInput) -> dict:
    out: dict = {}
    import aws_sdk_observabilityadmin.types.encryption

    out["Encryption"] = aws_sdk_observabilityadmin.types.encryption.serialize_json(
        value["encryption"]
    )
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateS3TableIntegrationInput:
    out: CreateS3TableIntegrationInput = {}  # type: ignore[typeddict-item]
    if "Encryption" in data:
        import aws_sdk_observabilityadmin.types.encryption

        out["encryption"] = (
            aws_sdk_observabilityadmin.types.encryption.deserialize_json(
                data["Encryption"]
            )
        )
    else:
        raise DeserializationError("CreateS3TableIntegrationInput.encryption required")
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateS3TableIntegrationInput.role_arn required")
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    return out
