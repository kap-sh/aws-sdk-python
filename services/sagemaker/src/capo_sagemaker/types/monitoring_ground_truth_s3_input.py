"""Generated from Smithy shape ``com.amazonaws.sagemaker#MonitoringGroundTruthS3Input``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_s3_uri


class MonitoringGroundTruthS3Input(TypedDict, closed=True):
    s3_uri: NotRequired["capo_sagemaker.types.monitoring_s3_uri.MonitoringS3Uri"]
    """<p>The address of the Amazon S3 location of the ground truth labels.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringGroundTruthS3Input) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringGroundTruthS3Input:
    out: MonitoringGroundTruthS3Input = {}  # type: ignore[typeddict-item]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    return out
