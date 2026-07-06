"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListImagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.images
    import aws_sdk_sagemaker.types.next_token


class ListImagesResponse(TypedDict, closed=True):
    images: NotRequired["aws_sdk_sagemaker.types.images.Images"]
    """<p>A list of images and their properties.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of images, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImagesResponse) -> dict:
    out: dict = {}
    if "images" in value:
        import aws_sdk_sagemaker.types.images

        out["Images"] = aws_sdk_sagemaker.types.images.serialize_aws_json_1_1(
            value["images"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImagesResponse:
    out: ListImagesResponse = {}  # type: ignore[typeddict-item]
    if "Images" in data:
        import aws_sdk_sagemaker.types.images

        out["images"] = aws_sdk_sagemaker.types.images.deserialize_aws_json_1_1(
            data["Images"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
