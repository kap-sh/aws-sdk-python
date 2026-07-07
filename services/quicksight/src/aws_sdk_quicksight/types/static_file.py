"""Generated from Smithy shape ``com.amazonaws.quicksight#StaticFile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.image_static_file
    import aws_sdk_quicksight.types.spatial_static_file


class StaticFile(TypedDict, closed=True):
    image_static_file: NotRequired[
        "aws_sdk_quicksight.types.image_static_file.ImageStaticFile"
    ]
    """<p>The image static file.</p>"""
    spatial_static_file: NotRequired[
        "aws_sdk_quicksight.types.spatial_static_file.SpatialStaticFile"
    ]
    """<p>The spacial static file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticFile) -> dict:
    out: dict = {}
    if "image_static_file" in value:
        import aws_sdk_quicksight.types.image_static_file

        out["ImageStaticFile"] = (
            aws_sdk_quicksight.types.image_static_file.serialize_json(
                value["image_static_file"]
            )
        )
    if "spatial_static_file" in value:
        import aws_sdk_quicksight.types.spatial_static_file

        out["SpatialStaticFile"] = (
            aws_sdk_quicksight.types.spatial_static_file.serialize_json(
                value["spatial_static_file"]
            )
        )
    return out


def deserialize_json(data: dict) -> StaticFile:
    out: StaticFile = {}  # type: ignore[typeddict-item]
    if "ImageStaticFile" in data:
        import aws_sdk_quicksight.types.image_static_file

        out["image_static_file"] = (
            aws_sdk_quicksight.types.image_static_file.deserialize_json(
                data["ImageStaticFile"]
            )
        )
    if "SpatialStaticFile" in data:
        import aws_sdk_quicksight.types.spatial_static_file

        out["spatial_static_file"] = (
            aws_sdk_quicksight.types.spatial_static_file.deserialize_json(
                data["SpatialStaticFile"]
            )
        )
    return out
