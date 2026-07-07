"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DistributeImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.client_token
    import aws_sdk_imagebuilder.types.image_build_version_arn


class DistributeImageResponse(TypedDict, closed=True):
    client_token: NotRequired["aws_sdk_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image to be distributed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DistributeImageResponse) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    return out


def deserialize_json(data: dict) -> DistributeImageResponse:
    out: DistributeImageResponse = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    return out
