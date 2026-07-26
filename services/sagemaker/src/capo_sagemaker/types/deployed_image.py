"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeployedImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.container_image
    import capo_sagemaker.types.timestamp


class DeployedImage(TypedDict, closed=True):
    specified_image: NotRequired["capo_sagemaker.types.container_image.ContainerImage"]
    """<p>The image path you specified when you created the model.</p>"""
    resolved_image: NotRequired["capo_sagemaker.types.container_image.ContainerImage"]
    """<p>The specific digest path of the image hosted in this <code>ProductionVariant</code>.</p>"""
    resolution_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time when the image path for the model resolved to the <code>ResolvedImage</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployedImage) -> dict:
    out: dict = {}
    if "specified_image" in value:
        out["SpecifiedImage"] = value["specified_image"]
    if "resolved_image" in value:
        out["ResolvedImage"] = value["resolved_image"]
    if "resolution_time" in value:
        import capo_sagemaker.types.timestamp

        out["ResolutionTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["resolution_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeployedImage:
    out: DeployedImage = {}  # type: ignore[typeddict-item]
    if "SpecifiedImage" in data:
        out["specified_image"] = data["SpecifiedImage"]
    if "ResolvedImage" in data:
        out["resolved_image"] = data["ResolvedImage"]
    if "ResolutionTime" in data:
        import capo_sagemaker.types.timestamp

        out["resolution_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["ResolutionTime"]
            )
        )
    return out
