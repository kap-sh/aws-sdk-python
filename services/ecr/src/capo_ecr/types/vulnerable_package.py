"""Generated from Smithy shape ``com.amazonaws.ecr#VulnerablePackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.arch
    import capo_ecr.types.epoch
    import capo_ecr.types.file_path
    import capo_ecr.types.fixed_in_version
    import capo_ecr.types.package_manager
    import capo_ecr.types.release
    import capo_ecr.types.source_layer_hash
    import capo_ecr.types.version
    import capo_ecr.types.vulnerable_package_name


class VulnerablePackage(TypedDict, closed=True):
    arch: NotRequired["capo_ecr.types.arch.Arch"]
    """<p>The architecture of the vulnerable package.</p>"""
    epoch: NotRequired["capo_ecr.types.epoch.Epoch"]
    """<p>The epoch of the vulnerable package.</p>"""
    file_path: NotRequired["capo_ecr.types.file_path.FilePath"]
    """<p>The file path of the vulnerable package.</p>"""
    name: NotRequired["capo_ecr.types.vulnerable_package_name.VulnerablePackageName"]
    """<p>The name of the vulnerable package.</p>"""
    package_manager: NotRequired["capo_ecr.types.package_manager.PackageManager"]
    """<p>The package manager of the vulnerable package.</p>"""
    release: NotRequired["capo_ecr.types.release.Release"]
    """<p>The release of the vulnerable package.</p>"""
    source_layer_hash: NotRequired["capo_ecr.types.source_layer_hash.SourceLayerHash"]
    """<p>The source layer hash of the vulnerable package.</p>"""
    version: NotRequired["capo_ecr.types.version.Version"]
    """<p>The version of the vulnerable package.</p>"""
    fixed_in_version: NotRequired["capo_ecr.types.fixed_in_version.FixedInVersion"]
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
    if data.get("arch") is not None:
        out["arch"] = data["arch"]
    if data.get("epoch") is not None:
        out["epoch"] = data["epoch"]
    if data.get("filePath") is not None:
        out["file_path"] = data["filePath"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("packageManager") is not None:
        out["package_manager"] = data["packageManager"]
    if data.get("release") is not None:
        out["release"] = data["release"]
    if data.get("sourceLayerHash") is not None:
        out["source_layer_hash"] = data["sourceLayerHash"]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("fixedInVersion") is not None:
        out["fixed_in_version"] = data["fixedInVersion"]
    return out
