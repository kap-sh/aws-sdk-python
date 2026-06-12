"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEntitiesDetectionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.entities_detection_job_properties


class DescribeEntitiesDetectionJobResponse(TypedDict):
    entities_detection_job_properties: NotRequired[
        "aws_sdk_comprehend.types.entities_detection_job_properties.EntitiesDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with an entities detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntitiesDetectionJobResponse) -> dict:
    out: dict = {}
    if "entities_detection_job_properties" in value:
        import aws_sdk_comprehend.types.entities_detection_job_properties

        out["EntitiesDetectionJobProperties"] = (
            aws_sdk_comprehend.types.entities_detection_job_properties.serialize_aws_json_1_1(
                value["entities_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntitiesDetectionJobResponse:
    out: DescribeEntitiesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "EntitiesDetectionJobProperties" in data:
        import aws_sdk_comprehend.types.entities_detection_job_properties

        out["entities_detection_job_properties"] = (
            aws_sdk_comprehend.types.entities_detection_job_properties.deserialize_aws_json_1_1(
                data["EntitiesDetectionJobProperties"]
            )
        )
    return out
