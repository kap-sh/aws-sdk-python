"""Generated from Smithy shape ``com.amazonaws.ecr#AwsEcrContainerImageDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.arch
    import aws_sdk_ecr.types.author
    import aws_sdk_ecr.types.date
    import aws_sdk_ecr.types.image_digest
    import aws_sdk_ecr.types.image_tags_list
    import aws_sdk_ecr.types.in_use_count
    import aws_sdk_ecr.types.platform
    import aws_sdk_ecr.types.registry_id
    import aws_sdk_ecr.types.repository_name


class AwsEcrContainerImageDetails(TypedDict):
    architecture: NotRequired["aws_sdk_ecr.types.arch.Arch"]
    """<p>The architecture of the Amazon ECR container image.</p>"""
    author: NotRequired["aws_sdk_ecr.types.author.Author"]
    """<p>The image author of the Amazon ECR container image.</p>"""
    image_hash: NotRequired["aws_sdk_ecr.types.image_digest.ImageDigest"]
    """<p>The image hash of the Amazon ECR container image.</p>"""
    image_tags: NotRequired["aws_sdk_ecr.types.image_tags_list.ImageTagsList"]
    """<p>The image tags attached to the Amazon ECR container image.</p>"""
    platform: NotRequired["aws_sdk_ecr.types.platform.Platform"]
    """<p>The platform of the Amazon ECR container image.</p>"""
    pushed_at: NotRequired["aws_sdk_ecr.types.date.Date"]
    """<p>The date and time the Amazon ECR container image was pushed.</p>"""
    last_in_use_at: NotRequired["aws_sdk_ecr.types.date.Date"]
    """<p>The most recent date and time a cluster was running the image.</p>"""
    in_use_count: NotRequired["aws_sdk_ecr.types.in_use_count.InUseCount"]
    """<p>The number of Amazon ECS or Amazon EKS clusters currently running the image.</p>"""
    registry: NotRequired["aws_sdk_ecr.types.registry_id.RegistryId"]
    """<p>The registry the Amazon ECR container image belongs to.</p>"""
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository the Amazon ECR container image resides in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsEcrContainerImageDetails) -> dict:
    out: dict = {}
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "author" in value:
        out["author"] = value["author"]
    if "image_hash" in value:
        out["imageHash"] = value["image_hash"]
    if "image_tags" in value:
        import aws_sdk_ecr.types.image_tags_list

        out["imageTags"] = aws_sdk_ecr.types.image_tags_list.serialize_aws_json_1_1(
            value["image_tags"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "pushed_at" in value:
        import aws_sdk_ecr.types.date

        out["pushedAt"] = aws_sdk_ecr.types.date.serialize_aws_json_1_1(
            value["pushed_at"]
        )
    if "last_in_use_at" in value:
        import aws_sdk_ecr.types.date

        out["lastInUseAt"] = aws_sdk_ecr.types.date.serialize_aws_json_1_1(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        out["inUseCount"] = value["in_use_count"]
    if "registry" in value:
        out["registry"] = value["registry"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AwsEcrContainerImageDetails:
    out: AwsEcrContainerImageDetails = {}  # type: ignore[typeddict-item]
    if "architecture" in data:
        out["architecture"] = data["architecture"]
    if "author" in data:
        out["author"] = data["author"]
    if "imageHash" in data:
        out["image_hash"] = data["imageHash"]
    if "imageTags" in data:
        import aws_sdk_ecr.types.image_tags_list

        out["image_tags"] = aws_sdk_ecr.types.image_tags_list.deserialize_aws_json_1_1(
            data["imageTags"]
        )
    if "platform" in data:
        out["platform"] = data["platform"]
    if "pushedAt" in data:
        import aws_sdk_ecr.types.date

        out["pushed_at"] = aws_sdk_ecr.types.date.deserialize_aws_json_1_1(
            data["pushedAt"]
        )
    if "lastInUseAt" in data:
        import aws_sdk_ecr.types.date

        out["last_in_use_at"] = aws_sdk_ecr.types.date.deserialize_aws_json_1_1(
            data["lastInUseAt"]
        )
    if "inUseCount" in data:
        out["in_use_count"] = data["inUseCount"]
    if "registry" in data:
        out["registry"] = data["registry"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    return out
