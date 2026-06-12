"""Generated from Smithy shape ``com.amazonaws.lightsail#PrivateRegistryAccessRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.container_service_ecr_image_puller_role_request


class PrivateRegistryAccessRequest(TypedDict):
    ecr_image_puller_role: NotRequired[
        "aws_sdk_lightsail.types.container_service_ecr_image_puller_role_request.ContainerServiceECRImagePullerRoleRequest"
    ]
    """<p>An object to describe a request to activate or deactivate the role that you can use to grant an Amazon Lightsail container service access to Amazon Elastic Container Registry (Amazon ECR) private repositories.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateRegistryAccessRequest) -> dict:
    out: dict = {}
    if "ecr_image_puller_role" in value:
        import aws_sdk_lightsail.types.container_service_ecr_image_puller_role_request

        out["ecrImagePullerRole"] = (
            aws_sdk_lightsail.types.container_service_ecr_image_puller_role_request.serialize_aws_json_1_1(
                value["ecr_image_puller_role"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateRegistryAccessRequest:
    out: PrivateRegistryAccessRequest = {}  # type: ignore[typeddict-item]
    if "ecrImagePullerRole" in data:
        import aws_sdk_lightsail.types.container_service_ecr_image_puller_role_request

        out["ecr_image_puller_role"] = (
            aws_sdk_lightsail.types.container_service_ecr_image_puller_role_request.deserialize_aws_json_1_1(
                data["ecrImagePullerRole"]
            )
        )
    return out
