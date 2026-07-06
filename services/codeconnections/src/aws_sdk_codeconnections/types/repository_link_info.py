"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositoryLinkInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.connection_arn
    import aws_sdk_codeconnections.types.kms_key_arn
    import aws_sdk_codeconnections.types.owner_id
    import aws_sdk_codeconnections.types.provider_type
    import aws_sdk_codeconnections.types.repository_link_arn
    import aws_sdk_codeconnections.types.repository_link_id
    import aws_sdk_codeconnections.types.repository_name


class RepositoryLinkInfo(TypedDict, closed=True):
    connection_arn: "aws_sdk_codeconnections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection associated with the repository link.</p>"""
    encryption_key_arn: NotRequired[
        "aws_sdk_codeconnections.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.</p>"""
    owner_id: "aws_sdk_codeconnections.types.owner_id.OwnerId"
    """<p>The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.</p>"""
    provider_type: "aws_sdk_codeconnections.types.provider_type.ProviderType"
    """<p>The provider type for the connection, such as GitHub, associated with the repository link.</p>"""
    repository_link_arn: (
        "aws_sdk_codeconnections.types.repository_link_arn.RepositoryLinkArn"
    )
    """<p>The Amazon Resource Name (ARN) of the repository link.</p>"""
    repository_link_id: (
        "aws_sdk_codeconnections.types.repository_link_id.RepositoryLinkId"
    )
    """<p>The ID of the repository link.</p>"""
    repository_name: "aws_sdk_codeconnections.types.repository_name.RepositoryName"
    """<p>The name of the repository associated with the repository link.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositoryLinkInfo) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    out["OwnerId"] = value["owner_id"]
    import aws_sdk_codeconnections.types.provider_type

    out["ProviderType"] = (
        aws_sdk_codeconnections.types.provider_type.serialize_aws_json_1_0(
            value["provider_type"]
        )
    )
    out["RepositoryLinkArn"] = value["repository_link_arn"]
    out["RepositoryLinkId"] = value["repository_link_id"]
    out["RepositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositoryLinkInfo:
    out: RepositoryLinkInfo = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError("RepositoryLinkInfo.connection_arn required")
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    else:
        raise DeserializationError("RepositoryLinkInfo.owner_id required")
    if "ProviderType" in data:
        import aws_sdk_codeconnections.types.provider_type

        out["provider_type"] = (
            aws_sdk_codeconnections.types.provider_type.deserialize_aws_json_1_0(
                data["ProviderType"]
            )
        )
    else:
        raise DeserializationError("RepositoryLinkInfo.provider_type required")
    if "RepositoryLinkArn" in data:
        out["repository_link_arn"] = data["RepositoryLinkArn"]
    else:
        raise DeserializationError("RepositoryLinkInfo.repository_link_arn required")
    if "RepositoryLinkId" in data:
        out["repository_link_id"] = data["RepositoryLinkId"]
    else:
        raise DeserializationError("RepositoryLinkInfo.repository_link_id required")
    if "RepositoryName" in data:
        out["repository_name"] = data["RepositoryName"]
    else:
        raise DeserializationError("RepositoryLinkInfo.repository_name required")
    return out
