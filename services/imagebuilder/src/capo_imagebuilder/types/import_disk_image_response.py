"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImportDiskImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_build_version_arn


class ImportDiskImageResponse(TypedDict, closed=True):
    client_token: NotRequired["capo_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    image_build_version_arn: NotRequired[
        "capo_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the output AMI that was created from the ISO disk file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDiskImageResponse) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    return out


def deserialize_json(data: dict) -> ImportDiskImageResponse:
    out: ImportDiskImageResponse = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    return out
