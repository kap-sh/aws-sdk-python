"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#MavenReference``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.maven_artifact_id
    import aws_sdk_kinesis_analytics_v2.types.maven_group_id
    import aws_sdk_kinesis_analytics_v2.types.maven_version


class MavenReference(TypedDict):
    group_id: "aws_sdk_kinesis_analytics_v2.types.maven_group_id.MavenGroupId"
    """<p>The group ID of the Maven reference.</p>"""
    artifact_id: "aws_sdk_kinesis_analytics_v2.types.maven_artifact_id.MavenArtifactId"
    """<p>The artifact ID of the Maven reference.</p>"""
    version: "aws_sdk_kinesis_analytics_v2.types.maven_version.MavenVersion"
    """<p>The version of the Maven reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MavenReference) -> dict:
    out: dict = {}
    out["GroupId"] = value["group_id"]
    out["ArtifactId"] = value["artifact_id"]
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MavenReference:
    out: MavenReference = {}  # type: ignore[typeddict-item]
    if "GroupId" in data:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("MavenReference.group_id required")
    if "ArtifactId" in data:
        out["artifact_id"] = data["ArtifactId"]
    else:
        raise DeserializationError("MavenReference.artifact_id required")
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        raise DeserializationError("MavenReference.version required")
    return out
