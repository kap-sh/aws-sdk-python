"""Generated from Smithy shape ``com.amazonaws.omics#DefinitionRepositoryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.connection_arn
    import aws_sdk_omics.types.full_repository_id
    import aws_sdk_omics.types.source_reference


class DefinitionRepositoryDetails(TypedDict, closed=True):
    connection_arn: NotRequired["aws_sdk_omics.types.connection_arn.ConnectionArn"]
    """<p>The Amazon Resource Name (ARN) of the connection to the source code repository.</p>"""
    full_repository_id: NotRequired[
        "aws_sdk_omics.types.full_repository_id.FullRepositoryId"
    ]
    """<p>The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.</p>"""
    source_reference: NotRequired[
        "aws_sdk_omics.types.source_reference.SourceReference"
    ]
    """<p>The source reference for the repository, such as a branch name, tag, or commit ID.</p>"""
    provider_type: NotRequired["str"]
    """<p>The provider type of the source code repository, such as Bitbucket, GitHub, GitHubEnterpriseServer, GitLab, and GitLabSelfManaged.</p>"""
    provider_endpoint: NotRequired["str"]
    """<p>The endpoint URL of the source code repository provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DefinitionRepositoryDetails) -> dict:
    out: dict = {}
    if "connection_arn" in value:
        out["connectionArn"] = value["connection_arn"]
    if "full_repository_id" in value:
        out["fullRepositoryId"] = value["full_repository_id"]
    if "source_reference" in value:
        import aws_sdk_omics.types.source_reference

        out["sourceReference"] = aws_sdk_omics.types.source_reference.serialize_json(
            value["source_reference"]
        )
    if "provider_type" in value:
        out["providerType"] = value["provider_type"]
    if "provider_endpoint" in value:
        out["providerEndpoint"] = value["provider_endpoint"]
    return out


def deserialize_json(data: dict) -> DefinitionRepositoryDetails:
    out: DefinitionRepositoryDetails = {}  # type: ignore[typeddict-item]
    if "connectionArn" in data:
        out["connection_arn"] = data["connectionArn"]
    if "fullRepositoryId" in data:
        out["full_repository_id"] = data["fullRepositoryId"]
    if "sourceReference" in data:
        import aws_sdk_omics.types.source_reference

        out["source_reference"] = aws_sdk_omics.types.source_reference.deserialize_json(
            data["sourceReference"]
        )
    if "providerType" in data:
        out["provider_type"] = data["providerType"]
    if "providerEndpoint" in data:
        out["provider_endpoint"] = data["providerEndpoint"]
    return out
