"""Generated from Smithy shape ``com.amazonaws.ecr#DescribeImageSigningStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier
    import capo_ecr.types.image_signing_status_list
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class DescribeImageSigningStatusResponse(TypedDict, closed=True):
    repository_name: NotRequired["capo_ecr.types.repository_name.RepositoryName"]
    """<p>The name of the repository.</p>"""
    image_id: NotRequired["capo_ecr.types.image_identifier.ImageIdentifier"]
    """<p>An object with identifying information for the image.</p>"""
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry.</p>"""
    signing_statuses: NotRequired[
        "capo_ecr.types.image_signing_status_list.ImageSigningStatusList"
    ]
    """<p>A list of signing statuses for the specified image. Each status corresponds to a signing profile.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageSigningStatusResponse) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "image_id" in value:
        import capo_ecr.types.image_identifier

        out["imageId"] = capo_ecr.types.image_identifier.serialize_aws_json_1_1(
            value["image_id"]
        )
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    if "signing_statuses" in value:
        import capo_ecr.types.image_signing_status_list

        out["signingStatuses"] = (
            capo_ecr.types.image_signing_status_list.serialize_aws_json_1_1(
                value["signing_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageSigningStatusResponse:
    out: DescribeImageSigningStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    if data.get("imageId") is not None:
        import capo_ecr.types.image_identifier

        out["image_id"] = capo_ecr.types.image_identifier.deserialize_aws_json_1_1(
            data["imageId"]
        )
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("signingStatuses") is not None:
        import capo_ecr.types.image_signing_status_list

        out["signing_statuses"] = (
            capo_ecr.types.image_signing_status_list.deserialize_aws_json_1_1(
                data["signingStatuses"]
            )
        )
    return out
