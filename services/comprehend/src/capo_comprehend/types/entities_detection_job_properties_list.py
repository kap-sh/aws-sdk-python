"""Generated from Smithy shape ``com.amazonaws.comprehend#EntitiesDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.entities_detection_job_properties

EntitiesDetectionJobPropertiesList: TypeAlias = list[
    "capo_comprehend.types.entities_detection_job_properties.EntitiesDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitiesDetectionJobPropertiesList) -> list:
    import capo_comprehend.types.entities_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.entities_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntitiesDetectionJobPropertiesList:
    import capo_comprehend.types.entities_detection_job_properties

    out: EntitiesDetectionJobPropertiesList = []
    for item in data:
        out.append(
            capo_comprehend.types.entities_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
