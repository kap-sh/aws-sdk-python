"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CustomArtifactConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.artifact_type
    import capo_kinesis_analytics_v2.types.maven_reference
    import capo_kinesis_analytics_v2.types.s3_content_location


class CustomArtifactConfigurationDescription(TypedDict, closed=True):
    artifact_type: NotRequired[
        "capo_kinesis_analytics_v2.types.artifact_type.ArtifactType"
    ]
    """<p> <code>UDF</code> stands for user-defined functions. This type of artifact must be in an S3 bucket. A <code>DEPENDENCY_JAR</code> can be in either Maven or an S3 bucket.</p>"""
    s3_content_location_description: NotRequired[
        "capo_kinesis_analytics_v2.types.s3_content_location.S3ContentLocation"
    ]
    maven_reference_description: NotRequired[
        "capo_kinesis_analytics_v2.types.maven_reference.MavenReference"
    ]
    """<p>The parameters that are required to specify a Maven dependency.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomArtifactConfigurationDescription) -> dict:
    out: dict = {}
    if "artifact_type" in value:
        import capo_kinesis_analytics_v2.types.artifact_type

        out["ArtifactType"] = (
            capo_kinesis_analytics_v2.types.artifact_type.serialize_aws_json_1_1(
                value["artifact_type"]
            )
        )
    if "s3_content_location_description" in value:
        import capo_kinesis_analytics_v2.types.s3_content_location

        out["S3ContentLocationDescription"] = (
            capo_kinesis_analytics_v2.types.s3_content_location.serialize_aws_json_1_1(
                value["s3_content_location_description"]
            )
        )
    if "maven_reference_description" in value:
        import capo_kinesis_analytics_v2.types.maven_reference

        out["MavenReferenceDescription"] = (
            capo_kinesis_analytics_v2.types.maven_reference.serialize_aws_json_1_1(
                value["maven_reference_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomArtifactConfigurationDescription:
    out: CustomArtifactConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "ArtifactType" in data:
        import capo_kinesis_analytics_v2.types.artifact_type

        out["artifact_type"] = (
            capo_kinesis_analytics_v2.types.artifact_type.deserialize_aws_json_1_1(
                data["ArtifactType"]
            )
        )
    if "S3ContentLocationDescription" in data:
        import capo_kinesis_analytics_v2.types.s3_content_location

        out["s3_content_location_description"] = (
            capo_kinesis_analytics_v2.types.s3_content_location.deserialize_aws_json_1_1(
                data["S3ContentLocationDescription"]
            )
        )
    if "MavenReferenceDescription" in data:
        import capo_kinesis_analytics_v2.types.maven_reference

        out["maven_reference_description"] = (
            capo_kinesis_analytics_v2.types.maven_reference.deserialize_aws_json_1_1(
                data["MavenReferenceDescription"]
            )
        )
    return out
