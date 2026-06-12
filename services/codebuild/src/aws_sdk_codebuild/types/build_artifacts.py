"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildArtifacts``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codebuild.types.bucket_owner_access
    import aws_sdk_codebuild.types.string
    import aws_sdk_codebuild.types.wrapper_boolean


class BuildArtifacts(TypedDict):
    location: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>Information about the location of the build artifacts.</p>"""
    sha256sum: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The SHA-256 hash of the build artifact.</p> <p>You can use this hash along with a checksum tool to confirm file integrity and authenticity.</p> <note> <p>This value is available only if the build project's <code>packaging</code> value is set to <code>ZIP</code>.</p> </note>"""
    md5sum: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p>The MD5 hash of the build artifact.</p> <p>You can use this hash along with a checksum tool to confirm file integrity and authenticity.</p> <note> <p>This value is available only if the build project's <code>packaging</code> value is set to <code>ZIP</code>.</p> </note>"""
    override_artifact_name: NotRequired[
        "aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. </p>"""
    encryption_disabled: NotRequired[
        "aws_sdk_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> Information that tells you if encryption for build artifacts is disabled. </p>"""
    artifact_identifier: NotRequired["aws_sdk_codebuild.types.string.String"]
    """<p> An identifier for this artifact definition. </p>"""
    bucket_owner_access: NotRequired[
        "aws_sdk_codebuild.types.bucket_owner_access.BucketOwnerAccess"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildArtifacts) -> dict:
    out: dict = {}
    if "location" in value:
        out["location"] = value["location"]
    if "sha256sum" in value:
        out["sha256sum"] = value["sha256sum"]
    if "md5sum" in value:
        out["md5sum"] = value["md5sum"]
    if "override_artifact_name" in value:
        out["overrideArtifactName"] = value["override_artifact_name"]
    if "encryption_disabled" in value:
        out["encryptionDisabled"] = value["encryption_disabled"]
    if "artifact_identifier" in value:
        out["artifactIdentifier"] = value["artifact_identifier"]
    if "bucket_owner_access" in value:
        import aws_sdk_codebuild.types.bucket_owner_access

        out["bucketOwnerAccess"] = (
            aws_sdk_codebuild.types.bucket_owner_access.serialize_aws_json_1_1(
                value["bucket_owner_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildArtifacts:
    out: BuildArtifacts = {}  # type: ignore[typeddict-item]
    if "location" in data:
        out["location"] = data["location"]
    if "sha256sum" in data:
        out["sha256sum"] = data["sha256sum"]
    if "md5sum" in data:
        out["md5sum"] = data["md5sum"]
    if "overrideArtifactName" in data:
        out["override_artifact_name"] = data["overrideArtifactName"]
    if "encryptionDisabled" in data:
        out["encryption_disabled"] = data["encryptionDisabled"]
    if "artifactIdentifier" in data:
        out["artifact_identifier"] = data["artifactIdentifier"]
    if "bucketOwnerAccess" in data:
        import aws_sdk_codebuild.types.bucket_owner_access

        out["bucket_owner_access"] = (
            aws_sdk_codebuild.types.bucket_owner_access.deserialize_aws_json_1_1(
                data["bucketOwnerAccess"]
            )
        )
    return out
