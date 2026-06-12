"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.comprehend_arn_name
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.model_status
    import aws_sdk_comprehend.types.timestamp
    import aws_sdk_comprehend.types.version_name


class EntityRecognizerSummary(TypedDict):
    recognizer_name: NotRequired[
        "aws_sdk_comprehend.types.comprehend_arn_name.ComprehendArnName"
    ]
    """<p> The name that you assigned the entity recognizer.</p>"""
    number_of_versions: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p> The number of versions you created.</p>"""
    latest_version_created_at: NotRequired[
        "aws_sdk_comprehend.types.timestamp.Timestamp"
    ]
    """<p> The time that the latest entity recognizer version was submitted for processing.</p>"""
    latest_version_name: NotRequired[
        "aws_sdk_comprehend.types.version_name.VersionName"
    ]
    """<p> The version name you assigned to the latest entity recognizer version.</p>"""
    latest_version_status: NotRequired[
        "aws_sdk_comprehend.types.model_status.ModelStatus"
    ]
    """<p> Provides the status of the latest entity recognizer version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerSummary) -> dict:
    out: dict = {}
    if "recognizer_name" in value:
        out["RecognizerName"] = value["recognizer_name"]
    if "number_of_versions" in value:
        out["NumberOfVersions"] = value["number_of_versions"]
    if "latest_version_created_at" in value:
        import aws_sdk_comprehend.types.timestamp

        out["LatestVersionCreatedAt"] = (
            aws_sdk_comprehend.types.timestamp.serialize_aws_json_1_1(
                value["latest_version_created_at"]
            )
        )
    if "latest_version_name" in value:
        out["LatestVersionName"] = value["latest_version_name"]
    if "latest_version_status" in value:
        import aws_sdk_comprehend.types.model_status

        out["LatestVersionStatus"] = (
            aws_sdk_comprehend.types.model_status.serialize_aws_json_1_1(
                value["latest_version_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerSummary:
    out: EntityRecognizerSummary = {}  # type: ignore[typeddict-item]
    if "RecognizerName" in data:
        out["recognizer_name"] = data["RecognizerName"]
    if "NumberOfVersions" in data:
        out["number_of_versions"] = data["NumberOfVersions"]
    if "LatestVersionCreatedAt" in data:
        import aws_sdk_comprehend.types.timestamp

        out["latest_version_created_at"] = (
            aws_sdk_comprehend.types.timestamp.deserialize_aws_json_1_1(
                data["LatestVersionCreatedAt"]
            )
        )
    if "LatestVersionName" in data:
        out["latest_version_name"] = data["LatestVersionName"]
    if "LatestVersionStatus" in data:
        import aws_sdk_comprehend.types.model_status

        out["latest_version_status"] = (
            aws_sdk_comprehend.types.model_status.deserialize_aws_json_1_1(
                data["LatestVersionStatus"]
            )
        )
    return out
