"""Generated from Smithy shape ``com.amazonaws.ecr#Repository``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.arn
    import aws_sdk_ecr.types.creation_timestamp
    import aws_sdk_ecr.types.encryption_configuration
    import aws_sdk_ecr.types.image_scanning_configuration
    import aws_sdk_ecr.types.image_tag_mutability
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filters
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.url


class Repository(TypedDict):
    repository_arn: NotRequired["aws_sdk_ecr.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the <code>arn:aws:ecr</code> namespace, followed by the region of the repository, Amazon Web Services account ID of the repository owner, repository namespace, and repository name. For example, <code>arn:aws:ecr:region:012345678910:repository-namespace/repository-name</code>.</p>"""
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository.</p>"""
    repository_uri: NotRequired["aws_sdk_ecr.types.url.Url"]
    """<p>The URI for the repository. You can use this URI for container image <code>push</code> and <code>pull</code> operations.</p>"""
    created_at: NotRequired["aws_sdk_ecr.types.creation_timestamp.CreationTimestamp"]
    """<p>The date and time, in JavaScript date format, when the repository was created.</p>"""
    image_tag_mutability: NotRequired[
        "aws_sdk_ecr.types.image_tag_mutability.ImageTagMutability"
    ]
    """<p>The tag mutability setting for the repository.</p>"""
    image_tag_mutability_exclusion_filters: NotRequired[
        "aws_sdk_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
    ]
    """<p>A list of filters that specify which image tags are excluded from the repository's image tag mutability setting.</p>"""
    image_scanning_configuration: NotRequired[
        "aws_sdk_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    encryption_configuration: NotRequired[
        "aws_sdk_ecr.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</p>"""


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
        import aws_sdk_ecr.types.creation_timestamp

        out["createdAt"] = aws_sdk_ecr.types.creation_timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "image_tag_mutability" in value:
        import aws_sdk_ecr.types.image_tag_mutability

        out["imageTagMutability"] = (
            aws_sdk_ecr.types.image_tag_mutability.serialize_aws_json_1_1(
                value["image_tag_mutability"]
            )
        )
    if "image_tag_mutability_exclusion_filters" in value:
        import aws_sdk_ecr.types.image_tag_mutability_exclusion_filters

        out["imageTagMutabilityExclusionFilters"] = (
            aws_sdk_ecr.types.image_tag_mutability_exclusion_filters.serialize_aws_json_1_1(
                value["image_tag_mutability_exclusion_filters"]
            )
        )
    if "image_scanning_configuration" in value:
        import aws_sdk_ecr.types.image_scanning_configuration

        out["imageScanningConfiguration"] = (
            aws_sdk_ecr.types.image_scanning_configuration.serialize_aws_json_1_1(
                value["image_scanning_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import aws_sdk_ecr.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_ecr.types.encryption_configuration.serialize_aws_json_1_1(
                value["encryption_configuration"]
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
        import aws_sdk_ecr.types.creation_timestamp

        out["created_at"] = (
            aws_sdk_ecr.types.creation_timestamp.deserialize_aws_json_1_1(
                data["createdAt"]
            )
        )
    if "imageTagMutability" in data:
        import aws_sdk_ecr.types.image_tag_mutability

        out["image_tag_mutability"] = (
            aws_sdk_ecr.types.image_tag_mutability.deserialize_aws_json_1_1(
                data["imageTagMutability"]
            )
        )
    if "imageTagMutabilityExclusionFilters" in data:
        import aws_sdk_ecr.types.image_tag_mutability_exclusion_filters

        out["image_tag_mutability_exclusion_filters"] = (
            aws_sdk_ecr.types.image_tag_mutability_exclusion_filters.deserialize_aws_json_1_1(
                data["imageTagMutabilityExclusionFilters"]
            )
        )
    if "imageScanningConfiguration" in data:
        import aws_sdk_ecr.types.image_scanning_configuration

        out["image_scanning_configuration"] = (
            aws_sdk_ecr.types.image_scanning_configuration.deserialize_aws_json_1_1(
                data["imageScanningConfiguration"]
            )
        )
    if "encryptionConfiguration" in data:
        import aws_sdk_ecr.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_ecr.types.encryption_configuration.deserialize_aws_json_1_1(
                data["encryptionConfiguration"]
            )
        )
    return out
