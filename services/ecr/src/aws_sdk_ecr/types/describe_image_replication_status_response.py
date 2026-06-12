"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeImageReplicationStatusResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_identifier
    import aws_sdk_ecr.types.image_replication_status_list
    import aws_sdk_ecr.types.repository_name


class DescribeImageReplicationStatusResponse(TypedDict):
    repository_name: NotRequired["aws_sdk_ecr.types.repository_name.RepositoryName"]
    """<p>The repository name associated with the request.</p>"""
    image_id: NotRequired["aws_sdk_ecr.types.image_identifier.ImageIdentifier"]
    replication_statuses: NotRequired[
        "aws_sdk_ecr.types.image_replication_status_list.ImageReplicationStatusList"
    ]
    """<p>The replication status details for the images in the specified repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageReplicationStatusResponse) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_id" in value:
        import aws_sdk_ecr.types.image_identifier

        out["imageId"] = aws_sdk_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "replication_statuses" in value:
        import aws_sdk_ecr.types.image_replication_status_list

        out["replicationStatuses"] = (
            aws_sdk_ecr.types.image_replication_status_list.serialize_aws_json_1_1(
                value["replication_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageReplicationStatusResponse:
    out: DescribeImageReplicationStatusResponse = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "imageId" in data:
        import aws_sdk_ecr.types.image_identifier

        out["image_id"] = aws_sdk_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if "replicationStatuses" in data:
        import aws_sdk_ecr.types.image_replication_status_list

        out["replication_statuses"] = (
            aws_sdk_ecr.types.image_replication_status_list.deserialize_aws_json_1_1(
                data["replicationStatuses"]
            )
        )
    return out
