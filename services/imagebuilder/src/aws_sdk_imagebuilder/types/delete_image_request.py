"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_build_version_arn


class DeleteImageRequest(TypedDict, closed=True):
    image_build_version_arn: (
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Image Builder image resource to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImageRequest:
    out: DeleteImageRequest = {}  # type: ignore[typeddict-item]
    return out
