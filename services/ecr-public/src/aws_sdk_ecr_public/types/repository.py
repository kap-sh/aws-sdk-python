"""Generated from Smithy shape ``com.amazonaws.ecrpublic#Repository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.arn
    import aws_sdk_ecr_public.types.creation_timestamp
    import aws_sdk_ecr_public.types.registry_id
    import aws_sdk_ecr_public.types.repository_name
    import aws_sdk_ecr_public.types.url


class Repository(TypedDict, closed=True):
    repository_arn: NotRequired["aws_sdk_ecr_public.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the <code>arn:aws:ecr</code> namespace, followed by the region of the repository, Amazon Web Services account ID of the repository owner, repository namespace, and repository name. For example, <code>arn:aws:ecr:region:012345678910:repository/test</code>.</p>"""
    registry_id: NotRequired["aws_sdk_ecr_public.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID that's associated with the public registry that contains the repository.</p>"""
    repository_name: NotRequired[
        "aws_sdk_ecr_public.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository.</p>"""
    repository_uri: NotRequired["aws_sdk_ecr_public.types.url.Url"]
    """<p>The URI for the repository. You can use this URI for container image <code>push</code> and <code>pull</code> operations.</p>"""
    created_at: NotRequired[
        "aws_sdk_ecr_public.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>The date and time, in JavaScript date format, when the repository was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Repository) -> dict:
    out: dict = {}
    if "repository_arn" in value:
        out["repositoryArn"] = value["repository_arn"]
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "repository_uri" in value:
        out["repositoryUri"] = value["repository_uri"]
    if "created_at" in value:
        import aws_sdk_ecr_public.types.creation_timestamp

        out["createdAt"] = (
            aws_sdk_ecr_public.types.creation_timestamp.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Repository:
    out: Repository = {}  # type: ignore[typeddict-item]
    if "repositoryArn" in data:
        out["repository_arn"] = data["repositoryArn"]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "repositoryUri" in data:
        out["repository_uri"] = data["repositoryUri"]
    if "createdAt" in data:
        import aws_sdk_ecr_public.types.creation_timestamp

        out["created_at"] = (
            aws_sdk_ecr_public.types.creation_timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    return out
