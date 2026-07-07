"""Generated from Smithy shape ``com.amazonaws.panorama#PackageImportJobInputConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.package_version_input_config


class PackageImportJobInputConfig(TypedDict, closed=True):
    package_version_input_config: NotRequired[
        "aws_sdk_panorama.types.package_version_input_config.PackageVersionInputConfig"
    ]
    """<p>The package version's input configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageImportJobInputConfig) -> dict:
    out: dict = {}
    if "package_version_input_config" in value:
        import aws_sdk_panorama.types.package_version_input_config

        out["PackageVersionInputConfig"] = (
            aws_sdk_panorama.types.package_version_input_config.serialize_json(
                value["package_version_input_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageImportJobInputConfig:
    out: PackageImportJobInputConfig = {}  # type: ignore[typeddict-item]
    if "PackageVersionInputConfig" in data:
        import aws_sdk_panorama.types.package_version_input_config

        out["package_version_input_config"] = (
            aws_sdk_panorama.types.package_version_input_config.deserialize_json(
                data["PackageVersionInputConfig"]
            )
        )
    return out
