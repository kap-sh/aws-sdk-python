"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CustomArtifactConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.artifact_type
    import aws_sdk_kinesis_analytics_v2.types.maven_reference
    import aws_sdk_kinesis_analytics_v2.types.s3_content_location


class CustomArtifactConfiguration(TypedDict):
    artifact_type: "aws_sdk_kinesis_analytics_v2.types.artifact_type.ArtifactType"
    """<p> <code>UDF</code> stands for user-defined functions. This type of artifact must be in an S3 bucket. A <code>DEPENDENCY_JAR</code> can be in either Maven or an S3 bucket.</p>"""
    s3_content_location: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.s3_content_location.S3ContentLocation"
    ]
    maven_reference: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.maven_reference.MavenReference"
    ]
    """<p>The parameters required to fully specify a Maven reference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomArtifactConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.artifact_type

    out["ArtifactType"] = (
        aws_sdk_kinesis_analytics_v2.types.artifact_type.serialize_aws_json_1_1(
            value["artifact_type"]
        )
    )
    if "s3_content_location" in value:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_location

        out["S3ContentLocation"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_location.serialize_aws_json_1_1(
                value["s3_content_location"]
            )
        )
    if "maven_reference" in value:
        import aws_sdk_kinesis_analytics_v2.types.maven_reference

        out["MavenReference"] = (
            aws_sdk_kinesis_analytics_v2.types.maven_reference.serialize_aws_json_1_1(
                value["maven_reference"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomArtifactConfiguration:
    out: CustomArtifactConfiguration = {}  # type: ignore[typeddict-item]
    if "ArtifactType" in data:
        import aws_sdk_kinesis_analytics_v2.types.artifact_type

        out["artifact_type"] = (
            aws_sdk_kinesis_analytics_v2.types.artifact_type.deserialize_aws_json_1_1(
                data["ArtifactType"]
            )
        )
    else:
        raise DeserializationError("CustomArtifactConfiguration.artifact_type required")
    if "S3ContentLocation" in data:
        import aws_sdk_kinesis_analytics_v2.types.s3_content_location

        out["s3_content_location"] = (
            aws_sdk_kinesis_analytics_v2.types.s3_content_location.deserialize_aws_json_1_1(
                data["S3ContentLocation"]
            )
        )
    if "MavenReference" in data:
        import aws_sdk_kinesis_analytics_v2.types.maven_reference

        out["maven_reference"] = (
            aws_sdk_kinesis_analytics_v2.types.maven_reference.deserialize_aws_json_1_1(
                data["MavenReference"]
            )
        )
    return out
