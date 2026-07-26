"""Generated from Smithy shape ``com.amazonaws.ecr#ResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.aws_ecr_container_image_details


class ResourceDetails(TypedDict, closed=True):
    aws_ecr_container_image: NotRequired[
        "capo_ecr.types.aws_ecr_container_image_details.AwsEcrContainerImageDetails"
    ]
    """<p>An object that contains details about the Amazon ECR container image involved in the finding.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceDetails) -> dict:
    out: dict = {}
    if "aws_ecr_container_image" in value:
        import capo_ecr.types.aws_ecr_container_image_details

        out["awsEcrContainerImage"] = (
            capo_ecr.types.aws_ecr_container_image_details.serialize_aws_json_1_1(
                value["aws_ecr_container_image"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceDetails:
    out: ResourceDetails = {}  # type: ignore[typeddict-item]
    if "awsEcrContainerImage" in data:
        import capo_ecr.types.aws_ecr_container_image_details

        out["aws_ecr_container_image"] = (
            capo_ecr.types.aws_ecr_container_image_details.deserialize_aws_json_1_1(
                data["awsEcrContainerImage"]
            )
        )
    return out
