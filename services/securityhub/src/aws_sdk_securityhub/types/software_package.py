"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwarePackage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class SoftwarePackage(TypedDict, closed=True):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the software package.</p>"""
    version: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The version of the software package.</p>"""
    epoch: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The epoch of the software package.</p>"""
    release: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The release of the software package.</p>"""
    architecture: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The architecture used for the software package.</p>"""
    package_manager: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The source of the package.</p>"""
    file_path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The file system path to the package manager inventory file.</p>"""
    fixed_in_version: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The version of the software package in which the vulnerability has been resolved. </p>"""
    remediation: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Describes the actions a customer can take to resolve the vulnerability in the software package. </p>"""
    source_layer_hash: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The source layer hash of the vulnerable package. </p>"""
    source_layer_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the source layer. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwarePackage) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "epoch" in value:
        out["Epoch"] = value["epoch"]
    if "release" in value:
        out["Release"] = value["release"]
    if "architecture" in value:
        out["Architecture"] = value["architecture"]
    if "package_manager" in value:
        out["PackageManager"] = value["package_manager"]
    if "file_path" in value:
        out["FilePath"] = value["file_path"]
    if "fixed_in_version" in value:
        out["FixedInVersion"] = value["fixed_in_version"]
    if "remediation" in value:
        out["Remediation"] = value["remediation"]
    if "source_layer_hash" in value:
        out["SourceLayerHash"] = value["source_layer_hash"]
    if "source_layer_arn" in value:
        out["SourceLayerArn"] = value["source_layer_arn"]
    return out


def deserialize_json(data: dict) -> SoftwarePackage:
    out: SoftwarePackage = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Epoch" in data:
        out["epoch"] = data["Epoch"]
    if "Release" in data:
        out["release"] = data["Release"]
    if "Architecture" in data:
        out["architecture"] = data["Architecture"]
    if "PackageManager" in data:
        out["package_manager"] = data["PackageManager"]
    if "FilePath" in data:
        out["file_path"] = data["FilePath"]
    if "FixedInVersion" in data:
        out["fixed_in_version"] = data["FixedInVersion"]
    if "Remediation" in data:
        out["remediation"] = data["Remediation"]
    if "SourceLayerHash" in data:
        out["source_layer_hash"] = data["SourceLayerHash"]
    if "SourceLayerArn" in data:
        out["source_layer_arn"] = data["SourceLayerArn"]
    return out
