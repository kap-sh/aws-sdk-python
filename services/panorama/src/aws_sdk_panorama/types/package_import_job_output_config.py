"""Generated from Smithy shape ``com.amazonaws.panorama#PackageImportJobOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_panorama.types.package_version_output_config


class PackageImportJobOutputConfig(TypedDict):
    package_version_output_config: NotRequired[
        "aws_sdk_panorama.types.package_version_output_config.PackageVersionOutputConfig"
    ]
    """<p>The package version's output configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageImportJobOutputConfig) -> dict:
    out: dict = {}
    if "package_version_output_config" in value:
        import aws_sdk_panorama.types.package_version_output_config

        out["PackageVersionOutputConfig"] = (
            aws_sdk_panorama.types.package_version_output_config.serialize_json(
                value["package_version_output_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> PackageImportJobOutputConfig:
    out: PackageImportJobOutputConfig = {}  # type: ignore[typeddict-item]
    if "PackageVersionOutputConfig" in data:
        import aws_sdk_panorama.types.package_version_output_config

        out["package_version_output_config"] = (
            aws_sdk_panorama.types.package_version_output_config.deserialize_json(
                data["PackageVersionOutputConfig"]
            )
        )
    return out
