"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConnectorV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.client_token
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.provider_configuration
    import aws_sdk_securityhub.types.tag_map


class CreateConnectorV2Request(TypedDict):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique name of the connectorV2.</p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The description of the connectorV2.</p>"""
    provider: NotRequired[
        "aws_sdk_securityhub.types.provider_configuration.ProviderConfiguration"
    ]
    """<p>The third-party provider’s service configuration.</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of KMS key used to encrypt secrets for the connectorV2.</p>"""
    tags: NotRequired["aws_sdk_securityhub.types.tag_map.TagMap"]
    """<p>The tags to add to the connectorV2 when you create.</p>"""
    client_token: NotRequired["aws_sdk_securityhub.types.client_token.ClientToken"]
    """<p>A unique identifier used to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConnectorV2Request) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "provider" in value:
        import aws_sdk_securityhub.types.provider_configuration

        out["Provider"] = (
            aws_sdk_securityhub.types.provider_configuration.serialize_json(
                value["provider"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_securityhub.types.tag_map

        out["Tags"] = aws_sdk_securityhub.types.tag_map.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateConnectorV2Request:
    out: CreateConnectorV2Request = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Provider" in data:
        import aws_sdk_securityhub.types.provider_configuration

        out["provider"] = (
            aws_sdk_securityhub.types.provider_configuration.deserialize_json(
                data["Provider"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "Tags" in data:
        import aws_sdk_securityhub.types.tag_map

        out["tags"] = aws_sdk_securityhub.types.tag_map.deserialize_json(data["Tags"])
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
