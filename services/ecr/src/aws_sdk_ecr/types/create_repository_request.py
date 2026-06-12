"""Generated from Smithy shape ``com.amazonaws.ecr#CreateRepositoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.encryption_configuration
    import aws_sdk_ecr.types.image_scanning_configuration
    import aws_sdk_ecr.types.image_tag_mutability
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filters
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name
    import aws_sdk_ecr.types.tag_list


class CreateRepositoryRequest(TypedDict):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry to create the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "aws_sdk_ecr.types.repository_name.RepositoryName"
    """<p>The name to use for the repository. The repository name may be specified on its own (such as <code>nginx-web-app</code>) or it can be prepended with a namespace to group the repository into a category (such as <code>project-a/nginx-web-app</code>).</p> <p>The repository name must start with a letter and can only contain lowercase letters, numbers, hyphens, underscores, and forward slashes.</p>"""
    tags: NotRequired["aws_sdk_ecr.types.tag_list.TagList"]
    """<p>The metadata that you apply to the repository to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters.</p>"""
    image_tag_mutability: NotRequired[
        "aws_sdk_ecr.types.image_tag_mutability.ImageTagMutability"
    ]
    """<p>The tag mutability setting for the repository. If this parameter is omitted, the default setting of <code>MUTABLE</code> will be used which will allow image tags to be overwritten. If <code>IMMUTABLE</code> is specified, all image tags within the repository will be immutable which will prevent them from being overwritten.</p>"""
    image_tag_mutability_exclusion_filters: NotRequired[
        "aws_sdk_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
    ]
    """<p>A list of filters that specify which image tags should be excluded from the repository's image tag mutability setting.</p>"""
    image_scanning_configuration: NotRequired[
        "aws_sdk_ecr.types.image_scanning_configuration.ImageScanningConfiguration"
    ]
    """<important> <p>The <code>imageScanningConfiguration</code> parameter is being deprecated, in favor of specifying the image scanning configuration at the registry level. For more information, see <code>PutRegistryScanningConfiguration</code>.</p> </important> <p>The image scanning configuration for the repository. This determines whether images are scanned for known vulnerabilities after being pushed to the repository.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_ecr.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRepositoryRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    if "tags" in value:
        import aws_sdk_ecr.types.tag_list

        out["tags"] = aws_sdk_ecr.types.tag_list.serialize_aws_json_1_1(value["tags"])
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


def deserialize_aws_json_1_1(data: dict) -> CreateRepositoryRequest:
    out: CreateRepositoryRequest = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("CreateRepositoryRequest.repository_name required")
    if "tags" in data:
        import aws_sdk_ecr.types.tag_list

        out["tags"] = aws_sdk_ecr.types.tag_list.deserialize_aws_json_1_1(data["tags"])
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
