"""Generated from Smithy shape ``com.amazonaws.ecr#VulnerablePackage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.arch
    import aws_sdk_ecr.types.epoch
    import aws_sdk_ecr.types.file_path
    import aws_sdk_ecr.types.fixed_in_version
    import aws_sdk_ecr.types.package_manager
    import aws_sdk_ecr.types.release
    import aws_sdk_ecr.types.source_layer_hash
    import aws_sdk_ecr.types.version
    import aws_sdk_ecr.types.vulnerable_package_name


class VulnerablePackage(TypedDict):
    arch: NotRequired["aws_sdk_ecr.types.arch.Arch"]
    """<p>The architecture of the vulnerable package.</p>"""
    epoch: NotRequired["aws_sdk_ecr.types.epoch.Epoch"]
    """<p>The epoch of the vulnerable package.</p>"""
    file_path: NotRequired["aws_sdk_ecr.types.file_path.FilePath"]
    """<p>The file path of the vulnerable package.</p>"""
    name: NotRequired["aws_sdk_ecr.types.vulnerable_package_name.VulnerablePackageName"]
    """<p>The name of the vulnerable package.</p>"""
    package_manager: NotRequired["aws_sdk_ecr.types.package_manager.PackageManager"]
    """<p>The package manager of the vulnerable package.</p>"""
    release: NotRequired["aws_sdk_ecr.types.release.Release"]
    """<p>The release of the vulnerable package.</p>"""
    source_layer_hash: NotRequired[
        "aws_sdk_ecr.types.source_layer_hash.SourceLayerHash"
    ]
    """<p>The source layer hash of the vulnerable package.</p>"""
    version: NotRequired["aws_sdk_ecr.types.version.Version"]
    """<p>The version of the vulnerable package.</p>"""
    fixed_in_version: NotRequired["aws_sdk_ecr.types.fixed_in_version.FixedInVersion"]
    """<p>The version of the package that contains the vulnerability fix.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VulnerablePackage) -> dict:
    out: dict = {}
    if "arch" in value:
        out["arch"] = value["arch"]
    if "epoch" in value:
        out["epoch"] = value["epoch"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "name" in value:
        out["name"] = value["name"]
    if "package_manager" in value:
        out["packageManager"] = value["package_manager"]
    if "release" in value:
        out["release"] = value["release"]
    if "source_layer_hash" in value:
        out["sourceLayerHash"] = value["source_layer_hash"]
    if "version" in value:
        out["version"] = value["version"]
    if "fixed_in_version" in value:
        out["fixedInVersion"] = value["fixed_in_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> VulnerablePackage:
    out: VulnerablePackage = {}  # type: ignore[typeddict-item]
    if "arch" in data:
        out["arch"] = data["arch"]
    if "epoch" in data:
        out["epoch"] = data["epoch"]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    if "name" in data:
        out["name"] = data["name"]
    if "packageManager" in data:
        out["package_manager"] = data["packageManager"]
    if "release" in data:
        out["release"] = data["release"]
    if "sourceLayerHash" in data:
        out["source_layer_hash"] = data["sourceLayerHash"]
    if "version" in data:
        out["version"] = data["version"]
    if "fixedInVersion" in data:
        out["fixed_in_version"] = data["fixedInVersion"]
    return out
