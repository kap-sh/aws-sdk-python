"""Generated from Smithy shape ``com.amazonaws.inspector2#VulnerablePackage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.file_path
    import aws_sdk_inspector2.types.lambda_layer_arn
    import aws_sdk_inspector2.types.package_architecture
    import aws_sdk_inspector2.types.package_epoch
    import aws_sdk_inspector2.types.package_manager
    import aws_sdk_inspector2.types.package_name
    import aws_sdk_inspector2.types.package_release
    import aws_sdk_inspector2.types.package_version
    import aws_sdk_inspector2.types.source_layer_hash
    import aws_sdk_inspector2.types.vulnerable_package_remediation


class VulnerablePackage(TypedDict):
    name: "aws_sdk_inspector2.types.package_name.PackageName"
    """<p>The name of the vulnerable package.</p>"""
    version: "aws_sdk_inspector2.types.package_version.PackageVersion"
    """<p>The version of the vulnerable package.</p>"""
    source_layer_hash: NotRequired[
        "aws_sdk_inspector2.types.source_layer_hash.SourceLayerHash"
    ]
    """<p>The source layer hash of the vulnerable package.</p>"""
    epoch: "aws_sdk_inspector2.types.package_epoch.PackageEpoch"
    """<p>The epoch of the vulnerable package.</p>"""
    release: NotRequired["aws_sdk_inspector2.types.package_release.PackageRelease"]
    """<p>The release of the vulnerable package.</p>"""
    arch: NotRequired[
        "aws_sdk_inspector2.types.package_architecture.PackageArchitecture"
    ]
    """<p>The architecture of the vulnerable package.</p>"""
    package_manager: NotRequired[
        "aws_sdk_inspector2.types.package_manager.PackageManager"
    ]
    """<p>The package manager of the vulnerable package.</p>"""
    file_path: NotRequired["aws_sdk_inspector2.types.file_path.FilePath"]
    """<p>The file path of the vulnerable package.</p>"""
    fixed_in_version: NotRequired[
        "aws_sdk_inspector2.types.package_version.PackageVersion"
    ]
    """<p>The version of the package that contains the vulnerability fix.</p>"""
    remediation: NotRequired[
        "aws_sdk_inspector2.types.vulnerable_package_remediation.VulnerablePackageRemediation"
    ]
    """<p>The code to run in your environment to update packages with a fix available.</p>"""
    source_lambda_layer_arn: NotRequired[
        "aws_sdk_inspector2.types.lambda_layer_arn.LambdaLayerArn"
    ]
    """<p>The Amazon Resource Number (ARN) of the Amazon Web Services Lambda function affected by a finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VulnerablePackage) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["version"] = value["version"]
    if "source_layer_hash" in value:
        out["sourceLayerHash"] = value["source_layer_hash"]
    out["epoch"] = value.get("epoch", 0)
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
    if "source_lambda_layer_arn" in value:
        out["sourceLambdaLayerArn"] = value["source_lambda_layer_arn"]
    return out


def deserialize_json(data: dict) -> VulnerablePackage:
    out: VulnerablePackage = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("VulnerablePackage.name required")
    if "version" in data:
        out["version"] = data["version"]
    else:
        raise DeserializationError("VulnerablePackage.version required")
    if "sourceLayerHash" in data:
        out["source_layer_hash"] = data["sourceLayerHash"]
    if "epoch" in data:
        out["epoch"] = data["epoch"]
    else:
        out["epoch"] = 0
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
    if "sourceLambdaLayerArn" in data:
        out["source_lambda_layer_arn"] = data["sourceLambdaLayerArn"]
    return out
