"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.package_config


class EnvironmentConfig(TypedDict, closed=True):
    image_version: NotRequired["str"]
    """<p>The image version for the notebook run environment.</p>"""
    package_config: NotRequired["aws_sdk_datazone.types.package_config.PackageConfig"]
    """<p>The package configuration for the notebook run environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfig) -> dict:
    out: dict = {}
    if "image_version" in value:
        out["imageVersion"] = value["image_version"]
    if "package_config" in value:
        import aws_sdk_datazone.types.package_config

        out["packageConfig"] = aws_sdk_datazone.types.package_config.serialize_json(
            value["package_config"]
        )
    return out


def deserialize_json(data: dict) -> EnvironmentConfig:
    out: EnvironmentConfig = {}  # type: ignore[typeddict-item]
    if "imageVersion" in data:
        out["image_version"] = data["imageVersion"]
    if "packageConfig" in data:
        import aws_sdk_datazone.types.package_config

        out["package_config"] = aws_sdk_datazone.types.package_config.deserialize_json(
            data["packageConfig"]
        )
    return out
