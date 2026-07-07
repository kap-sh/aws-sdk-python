"""Generated from Smithy shape ``com.amazonaws.ecr#PutImageTagMutabilityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_tag_mutability
    import aws_sdk_ecr.types.image_tag_mutability_exclusion_filters
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class PutImageTagMutabilityResponse(TypedDict, closed=True):
    registry_id: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry ID associated with the request.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    image_tag_mutability: NotRequired[
        "aws_sdk_ecr.types.image_tag_mutability.ImageTagMutability"
    ]
    """<p>The image tag mutability setting for the repository.</p>"""
    image_tag_mutability_exclusion_filters: NotRequired[
        "aws_sdk_ecr.types.image_tag_mutability_exclusion_filters.ImageTagMutabilityExclusionFilters"
    ]
    """<p>The list of filters that specify which image tags are excluded from the repository's image tag mutability setting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutImageTagMutabilityResponse) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> PutImageTagMutabilityResponse:
    out: PutImageTagMutabilityResponse = {}  # type: ignore[typeddict-item]
    if "registryId" in data:
        out["registry_id"] = data["registryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
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
    return out
