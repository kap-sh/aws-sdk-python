"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.image_name


class DeleteImageRequest(TypedDict, closed=True):
    image_name: NotRequired["capo_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteImageRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteImageRequest:
    out: DeleteImageRequest = {}  # type: ignore[typeddict-item]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    return out
