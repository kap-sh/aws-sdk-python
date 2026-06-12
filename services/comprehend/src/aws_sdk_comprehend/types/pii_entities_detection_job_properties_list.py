"""Generated from Smithy shape ``com.amazonaws.comprehend#PiiEntitiesDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.pii_entities_detection_job_properties

PiiEntitiesDetectionJobPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.pii_entities_detection_job_properties.PiiEntitiesDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PiiEntitiesDetectionJobPropertiesList) -> list:
    import aws_sdk_comprehend.types.pii_entities_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.pii_entities_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PiiEntitiesDetectionJobPropertiesList:
    import aws_sdk_comprehend.types.pii_entities_detection_job_properties

    out: PiiEntitiesDetectionJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.pii_entities_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
