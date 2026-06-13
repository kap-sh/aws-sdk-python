"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEcrContainerImageDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.date_time_timestamp
    import aws_sdk_inspector2.types.image_hash
    import aws_sdk_inspector2.types.image_tag_list
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.platform


class AwsEcrContainerImageDetails(TypedDict):
    repository_name: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The name of the repository the Amazon ECR container image resides in.</p>"""
    image_tags: NotRequired["aws_sdk_inspector2.types.image_tag_list.ImageTagList"]
    """<p>The image tags attached to the Amazon ECR container image.</p>"""
    pushed_at: NotRequired[
        "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the Amazon ECR container image was pushed.</p>"""
    author: NotRequired["str"]
    """<p>The image author of the Amazon ECR container image.</p>"""
    architecture: NotRequired[
        "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    ]
    """<p>The architecture of the Amazon ECR container image.</p>"""
    image_hash: "aws_sdk_inspector2.types.image_hash.ImageHash"
    """<p>The image hash of the Amazon ECR container image.</p>"""
    registry: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The registry for the Amazon ECR container image.</p>"""
    platform: NotRequired["aws_sdk_inspector2.types.platform.Platform"]
    """<p>The platform of the Amazon ECR container image.</p>"""
    last_in_use_at: NotRequired[
        "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.</p>"""
    in_use_count: NotRequired["int"]
    """<p>The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrContainerImageDetails) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "image_tags" in value:
        import aws_sdk_inspector2.types.image_tag_list

        out["imageTags"] = aws_sdk_inspector2.types.image_tag_list.serialize_json(
            value["image_tags"]
        )
    if "pushed_at" in value:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["pushedAt"] = aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
            value["pushed_at"]
        )
    if "author" in value:
        out["author"] = value["author"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    out["imageHash"] = value["image_hash"]
    out["registry"] = value["registry"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "last_in_use_at" in value:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["lastInUseAt"] = (
            aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
                value["last_in_use_at"]
            )
        )
    if "in_use_count" in value:
        out["inUseCount"] = value["in_use_count"]
    return out


def deserialize_json(data: dict) -> AwsEcrContainerImageDetails:
    out: AwsEcrContainerImageDetails = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "AwsEcrContainerImageDetails.repository_name required"
        )
    if "imageTags" in data:
        import aws_sdk_inspector2.types.image_tag_list

        out["image_tags"] = aws_sdk_inspector2.types.image_tag_list.deserialize_json(
            data["imageTags"]
        )
    if "pushedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["pushed_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["pushedAt"]
            )
        )
    if "author" in data:
        out["author"] = data["author"]
    if "architecture" in data:
        out["architecture"] = data["architecture"]
    if "imageHash" in data:
        out["image_hash"] = data["imageHash"]
    else:
        raise DeserializationError("AwsEcrContainerImageDetails.image_hash required")
    if "registry" in data:
        out["registry"] = data["registry"]
    else:
        raise DeserializationError("AwsEcrContainerImageDetails.registry required")
    if "platform" in data:
        out["platform"] = data["platform"]
    if "lastInUseAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["last_in_use_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastInUseAt"]
            )
        )
    if "inUseCount" in data:
        out["in_use_count"] = data["inUseCount"]
    return out
