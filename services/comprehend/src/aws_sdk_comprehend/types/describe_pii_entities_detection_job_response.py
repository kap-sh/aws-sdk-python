"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribePiiEntitiesDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.pii_entities_detection_job_properties


class DescribePiiEntitiesDetectionJobResponse(TypedDict, closed=True):
    pii_entities_detection_job_properties: NotRequired[
        "aws_sdk_comprehend.types.pii_entities_detection_job_properties.PiiEntitiesDetectionJobProperties"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePiiEntitiesDetectionJobResponse) -> dict:
    out: dict = {}
    if "pii_entities_detection_job_properties" in value:
        import aws_sdk_comprehend.types.pii_entities_detection_job_properties

        out["PiiEntitiesDetectionJobProperties"] = (
            aws_sdk_comprehend.types.pii_entities_detection_job_properties.serialize_aws_json_1_1(
                value["pii_entities_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePiiEntitiesDetectionJobResponse:
    out: DescribePiiEntitiesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "PiiEntitiesDetectionJobProperties" in data:
        import aws_sdk_comprehend.types.pii_entities_detection_job_properties

        out["pii_entities_detection_job_properties"] = (
            aws_sdk_comprehend.types.pii_entities_detection_job_properties.deserialize_aws_json_1_1(
                data["PiiEntitiesDetectionJobProperties"]
            )
        )
    return out
