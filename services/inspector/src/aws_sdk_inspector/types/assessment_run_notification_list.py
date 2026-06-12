"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunNotificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.assessment_run_notification

AssessmentRunNotificationList: TypeAlias = list[
    "aws_sdk_inspector.types.assessment_run_notification.AssessmentRunNotification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunNotificationList) -> list:
    import aws_sdk_inspector.types.assessment_run_notification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector.types.assessment_run_notification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentRunNotificationList:
    import aws_sdk_inspector.types.assessment_run_notification

    out: AssessmentRunNotificationList = []
    for item in data:
        out.append(
            aws_sdk_inspector.types.assessment_run_notification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
