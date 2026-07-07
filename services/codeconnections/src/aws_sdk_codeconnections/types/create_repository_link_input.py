"""Generated from Smithy shape ``com.amazonaws.codeconnections#CreateRepositoryLinkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.connection_arn
    import aws_sdk_codeconnections.types.kms_key_arn
    import aws_sdk_codeconnections.types.owner_id
    import aws_sdk_codeconnections.types.repository_name
    import aws_sdk_codeconnections.types.tag_list


class CreateRepositoryLinkInput(TypedDict, closed=True):
    connection_arn: "aws_sdk_codeconnections.types.connection_arn.ConnectionArn"
    """<p>The Amazon Resource Name (ARN) of the connection to be associated with the repository link.</p>"""
    owner_id: "aws_sdk_codeconnections.types.owner_id.OwnerId"
    """<p>The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.</p>"""
    repository_name: "aws_sdk_codeconnections.types.repository_name.RepositoryName"
    """<p>The name of the repository to be associated with the repository link.</p>"""
    encryption_key_arn: NotRequired[
        "aws_sdk_codeconnections.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) encryption key for the repository to be associated with the repository link.</p>"""
    tags: NotRequired["aws_sdk_codeconnections.types.tag_list.TagList"]
    """<p>The tags for the repository to be associated with the repository link.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRepositoryLinkInput) -> dict:
    out: dict = {}
    out["ConnectionArn"] = value["connection_arn"]
    out["OwnerId"] = value["owner_id"]
    out["RepositoryName"] = value["repository_name"]
    if "encryption_key_arn" in value:
        out["EncryptionKeyArn"] = value["encryption_key_arn"]
    if "tags" in value:
        import aws_sdk_codeconnections.types.tag_list

        out["Tags"] = aws_sdk_codeconnections.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRepositoryLinkInput:
    out: CreateRepositoryLinkInput = {}  # type: ignore[typeddict-item]
    if "ConnectionArn" in data:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        raise DeserializationError("CreateRepositoryLinkInput.connection_arn required")
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    else:
        raise DeserializationError("CreateRepositoryLinkInput.owner_id required")
    if "RepositoryName" in data:
        out["repository_name"] = data["RepositoryName"]
    else:
        raise DeserializationError("CreateRepositoryLinkInput.repository_name required")
    if "EncryptionKeyArn" in data:
        out["encryption_key_arn"] = data["EncryptionKeyArn"]
    if "Tags" in data:
        import aws_sdk_codeconnections.types.tag_list

        out["tags"] = aws_sdk_codeconnections.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
