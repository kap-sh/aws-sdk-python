"""Generated from Smithy shape ``com.amazonaws.sagemaker#RSessionAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.custom_images
    import capo_sagemaker.types.resource_spec


class RSessionAppSettings(TypedDict, closed=True):
    default_resource_spec: NotRequired[
        "capo_sagemaker.types.resource_spec.ResourceSpec"
    ]
    custom_images: NotRequired["capo_sagemaker.types.custom_images.CustomImages"]
    """<p>A list of custom SageMaker AI images that are configured to run as a RSession app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RSessionAppSettings) -> dict:
    out: dict = {}
    if "default_resource_spec" in value:
        import capo_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            capo_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    if "custom_images" in value:
        import capo_sagemaker.types.custom_images

        out["CustomImages"] = capo_sagemaker.types.custom_images.serialize_aws_json_1_1(
            value["custom_images"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RSessionAppSettings:
    out: RSessionAppSettings = {}  # type: ignore[typeddict-item]
    if "DefaultResourceSpec" in data:
        import capo_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            capo_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    if "CustomImages" in data:
        import capo_sagemaker.types.custom_images

        out["custom_images"] = (
            capo_sagemaker.types.custom_images.deserialize_aws_json_1_1(
                data["CustomImages"]
            )
        )
    return out
