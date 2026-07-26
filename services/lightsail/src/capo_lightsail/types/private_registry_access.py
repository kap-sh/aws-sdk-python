"""Generated from Smithy shape ``com.amazonaws.lightsail#PrivateRegistryAccess``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.container_service_ecr_image_puller_role


class PrivateRegistryAccess(TypedDict, closed=True):
    ecr_image_puller_role: NotRequired[
        "capo_lightsail.types.container_service_ecr_image_puller_role.ContainerServiceECRImagePullerRole"
    ]
    """<p>An object that describes the activation status of the role that you can use to grant a Lightsail container service access to Amazon ECR private repositories. If the role is activated, the Amazon Resource Name (ARN) of the role is also listed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateRegistryAccess) -> dict:
    out: dict = {}
    if "ecr_image_puller_role" in value:
        import capo_lightsail.types.container_service_ecr_image_puller_role

        out["ecrImagePullerRole"] = (
            capo_lightsail.types.container_service_ecr_image_puller_role.serialize_aws_json_1_1(
                value["ecr_image_puller_role"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateRegistryAccess:
    out: PrivateRegistryAccess = {}  # type: ignore[typeddict-item]
    if "ecrImagePullerRole" in data:
        import capo_lightsail.types.container_service_ecr_image_puller_role

        out["ecr_image_puller_role"] = (
            capo_lightsail.types.container_service_ecr_image_puller_role.deserialize_aws_json_1_1(
                data["ecrImagePullerRole"]
            )
        )
    return out
