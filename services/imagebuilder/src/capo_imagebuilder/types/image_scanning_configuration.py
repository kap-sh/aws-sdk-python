"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanningConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.ecr_configuration
    import capo_imagebuilder.types.nullable_boolean


class ImageScanningConfiguration(TypedDict, closed=True):
    image_scanning_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>A setting that indicates whether Image Builder keeps a snapshot of the vulnerability scans that Amazon Inspector runs against the build instance when you create a new image.</p>"""
    ecr_configuration: NotRequired[
        "capo_imagebuilder.types.ecr_configuration.EcrConfiguration"
    ]
    """<p>Contains Amazon ECR settings for vulnerability scans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanningConfiguration) -> dict:
    out: dict = {}
    if "image_scanning_enabled" in value:
        out["imageScanningEnabled"] = value["image_scanning_enabled"]
    if "ecr_configuration" in value:
        import capo_imagebuilder.types.ecr_configuration

        out["ecrConfiguration"] = (
            capo_imagebuilder.types.ecr_configuration.serialize_json(
                value["ecr_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImageScanningConfiguration:
    out: ImageScanningConfiguration = {}  # type: ignore[typeddict-item]
    if "imageScanningEnabled" in data:
        out["image_scanning_enabled"] = data["imageScanningEnabled"]
    if "ecrConfiguration" in data:
        import capo_imagebuilder.types.ecr_configuration

        out["ecr_configuration"] = (
            capo_imagebuilder.types.ecr_configuration.deserialize_json(
                data["ecrConfiguration"]
            )
        )
    return out
