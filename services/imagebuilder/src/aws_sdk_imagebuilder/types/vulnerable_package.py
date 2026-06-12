"""Generated from Smithy shape ``com.amazonaws.imagebuilder#VulnerablePackage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.package_architecture
    import aws_sdk_imagebuilder.types.package_epoch
    import aws_sdk_imagebuilder.types.source_layer_hash


class VulnerablePackage(TypedDict):
    name: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The name of the vulnerable package.</p>"""
    version: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The version of the vulnerable package.</p>"""
    source_layer_hash: NotRequired[
        "aws_sdk_imagebuilder.types.source_layer_hash.SourceLayerHash"
    ]
    """<p>The source layer hash of the vulnerable package.</p>"""
    epoch: NotRequired["aws_sdk_imagebuilder.types.package_epoch.PackageEpoch"]
    """<p>The epoch of the vulnerable package.</p>"""
    release: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The release of the vulnerable package.</p>"""
    arch: NotRequired[
        "aws_sdk_imagebuilder.types.package_architecture.PackageArchitecture"
    ]
    """<p>The architecture of the vulnerable package.</p>"""
    package_manager: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The package manager of the vulnerable package.</p>"""
    file_path: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The file path of the vulnerable package.</p>"""
    fixed_in_version: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the package that contains the vulnerability fix.</p>"""
    remediation: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The code to run in your environment to update packages with a fix available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VulnerablePackage) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "version" in value:
        out["version"] = value["version"]
    if "source_layer_hash" in value:
        out["sourceLayerHash"] = value["source_layer_hash"]
    if "epoch" in value:
        out["epoch"] = value["epoch"]
    if "release" in value:
        out["release"] = value["release"]
    if "arch" in value:
        out["arch"] = value["arch"]
    if "package_manager" in value:
        out["packageManager"] = value["package_manager"]
    if "file_path" in value:
        out["filePath"] = value["file_path"]
    if "fixed_in_version" in value:
        out["fixedInVersion"] = value["fixed_in_version"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    return out


def deserialize_json(data: dict) -> VulnerablePackage:
    out: VulnerablePackage = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "version" in data:
        out["version"] = data["version"]
    if "sourceLayerHash" in data:
        out["source_layer_hash"] = data["sourceLayerHash"]
    if "epoch" in data:
        out["epoch"] = data["epoch"]
    if "release" in data:
        out["release"] = data["release"]
    if "arch" in data:
        out["arch"] = data["arch"]
    if "packageManager" in data:
        out["package_manager"] = data["packageManager"]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    if "fixedInVersion" in data:
        out["fixed_in_version"] = data["fixedInVersion"]
    if "remediation" in data:
        out["remediation"] = data["remediation"]
    return out
