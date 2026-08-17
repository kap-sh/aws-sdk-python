"""Generated from Smithy shape ``com.amazonaws.ecr#AwsEcrContainerImageDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.arch
    import capo_ecr.types.author
    import capo_ecr.types.date
    import capo_ecr.types.image_digest
    import capo_ecr.types.image_tags_list
    import capo_ecr.types.in_use_count
    import capo_ecr.types.platform
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class AwsEcrContainerImageDetails(TypedDict, closed=True):
    architecture: NotRequired["capo_ecr.types.arch.Arch"]
    """<p>The architecture of the Amazon ECR container image.</p>"""
    author: NotRequired["capo_ecr.types.author.Author"]
    """<p>The image author of the Amazon ECR container image.</p>"""
    image_hash: NotRequired["capo_ecr.types.image_digest.ImageDigest"]
    """<p>The image hash of the Amazon ECR container image.</p>"""
    image_tags: NotRequired["capo_ecr.types.image_tags_list.ImageTagsList"]
    """<p>The image tags attached to the Amazon ECR container image.</p>"""
    platform: NotRequired["capo_ecr.types.platform.Platform"]
    """<p>The platform of the Amazon ECR container image.</p>"""
    pushed_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The date and time the Amazon ECR container image was pushed.</p>"""
    last_in_use_at: NotRequired["capo_ecr.types.date.Date"]
    """<p>The most recent date and time a cluster was running the image.</p>"""
    in_use_count: NotRequired["capo_ecr.types.in_use_count.InUseCount"]
    """<p>The number of Amazon ECS or Amazon EKS clusters currently running the image.</p>"""
    registry: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The registry the Amazon ECR container image belongs to.</p>"""
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
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
        import capo_ecr.types.image_tags_list

        out["imageTags"] = capo_ecr.types.image_tags_list.serialize_aws_json_1_1(
            value["image_tags"]
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "pushed_at" in value:
        import capo_ecr.types.date

        out["pushedAt"] = capo_ecr.types.date.serialize_aws_json_1_1(value["pushed_at"])
    if "last_in_use_at" in value:
        import capo_ecr.types.date

        out["lastInUseAt"] = capo_ecr.types.date.serialize_aws_json_1_1(
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
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("author") is not None:
        out["author"] = data["author"]
    if data.get("imageHash") is not None:
        out["image_hash"] = data["imageHash"]
    if data.get("imageTags") is not None:
        import capo_ecr.types.image_tags_list

        out["image_tags"] = capo_ecr.types.image_tags_list.deserialize_aws_json_1_1(
            data["imageTags"]
        )
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("pushedAt") is not None:
        import capo_ecr.types.date

        out["pushed_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["pushedAt"]
        )
    if data.get("lastInUseAt") is not None:
        import capo_ecr.types.date

        out["last_in_use_at"] = capo_ecr.types.date.deserialize_aws_json_1_1(
            data["lastInUseAt"]
        )
    if data.get("inUseCount") is not None:
        out["in_use_count"] = data["inUseCount"]
    if data.get("registry") is not None:
        out["registry"] = data["registry"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    return out
