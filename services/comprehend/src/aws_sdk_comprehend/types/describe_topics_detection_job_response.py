"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeTopicsDetectionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.topics_detection_job_properties


class DescribeTopicsDetectionJobResponse(TypedDict):
    topics_detection_job_properties: NotRequired[
        "aws_sdk_comprehend.types.topics_detection_job_properties.TopicsDetectionJobProperties"
    ]
    """<p>The list of properties for the requested job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTopicsDetectionJobResponse) -> dict:
    out: dict = {}
    if "topics_detection_job_properties" in value:
        import aws_sdk_comprehend.types.topics_detection_job_properties

        out["TopicsDetectionJobProperties"] = (
            aws_sdk_comprehend.types.topics_detection_job_properties.serialize_aws_json_1_1(
                value["topics_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTopicsDetectionJobResponse:
    out: DescribeTopicsDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "TopicsDetectionJobProperties" in data:
        import aws_sdk_comprehend.types.topics_detection_job_properties

        out["topics_detection_job_properties"] = (
            aws_sdk_comprehend.types.topics_detection_job_properties.deserialize_aws_json_1_1(
                data["TopicsDetectionJobProperties"]
            )
        )
    return out
