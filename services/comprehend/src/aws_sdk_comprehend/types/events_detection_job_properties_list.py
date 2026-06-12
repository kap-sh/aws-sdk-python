"""Generated from Smithy shape ``com.amazonaws.comprehend#EventsDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.events_detection_job_properties

EventsDetectionJobPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.events_detection_job_properties.EventsDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventsDetectionJobPropertiesList) -> list:
    import aws_sdk_comprehend.types.events_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.events_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EventsDetectionJobPropertiesList:
    import aws_sdk_comprehend.types.events_detection_job_properties

    out: EventsDetectionJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.events_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
