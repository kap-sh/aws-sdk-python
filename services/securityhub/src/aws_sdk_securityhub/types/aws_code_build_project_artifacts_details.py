"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectArtifactsDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string


class AwsCodeBuildProjectArtifactsDetails(TypedDict):
    artifact_identifier: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>An identifier for the artifact definition.</p>"""
    encryption_disabled: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether to disable encryption on the artifact. Only valid when <code>Type</code> is <code>S3</code>.</p>"""
    location: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The name of the S3 bucket where the artifact is located.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when Type is S3. The name of the artifact. Used with <code>NamepaceType</code> and <code>Path</code> to determine the pattern for storing the artifact.</p>"""
    namespace_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The value to use for the namespace. Used with <code>Name</code> and <code>Path</code> to determine the pattern for storing the artifact.</p>"""
    override_artifact_name: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p>Whether the name specified in the buildspec file overrides the artifact name.</p>"""
    packaging: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The type of output artifact to create.</p>"""
    path: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Only used when <code>Type</code> is <code>S3</code>. The path to the artifact. Used with <code>Name</code> and <code>NamespaceType</code> to determine the pattern for storing the artifact.</p>"""
    type: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of build artifact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsCodeBuildProjectArtifactsDetails) -> dict:
    out: dict = {}
    if "artifact_identifier" in value:
        out["ArtifactIdentifier"] = value["artifact_identifier"]
    if "encryption_disabled" in value:
        out["EncryptionDisabled"] = value["encryption_disabled"]
    if "location" in value:
        out["Location"] = value["location"]
    if "name" in value:
        out["Name"] = value["name"]
    if "namespace_type" in value:
        out["NamespaceType"] = value["namespace_type"]
    if "override_artifact_name" in value:
        out["OverrideArtifactName"] = value["override_artifact_name"]
    if "packaging" in value:
        out["Packaging"] = value["packaging"]
    if "path" in value:
        out["Path"] = value["path"]
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_json(data: dict) -> AwsCodeBuildProjectArtifactsDetails:
    out: AwsCodeBuildProjectArtifactsDetails = {}  # type: ignore[typeddict-item]
    if "ArtifactIdentifier" in data:
        out["artifact_identifier"] = data["ArtifactIdentifier"]
    if "EncryptionDisabled" in data:
        out["encryption_disabled"] = data["EncryptionDisabled"]
    if "Location" in data:
        out["location"] = data["Location"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "NamespaceType" in data:
        out["namespace_type"] = data["NamespaceType"]
    if "OverrideArtifactName" in data:
        out["override_artifact_name"] = data["OverrideArtifactName"]
    if "Packaging" in data:
        out["packaging"] = data["Packaging"]
    if "Path" in data:
        out["path"] = data["Path"]
    if "Type" in data:
        out["type"] = data["Type"]
    return out
