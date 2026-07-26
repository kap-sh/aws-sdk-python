"""Generated from Smithy shape ``com.amazonaws.inspector#AssessmentRunNotificationSnsStatusCode``."""

from typing import Literal, TypeAlias, cast

AssessmentRunNotificationSnsStatusCode: TypeAlias = Literal[
    "SUCCESS",
    "TOPIC_DOES_NOT_EXIST",
    "ACCESS_DENIED",
    "INTERNAL_ERROR",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentRunNotificationSnsStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AssessmentRunNotificationSnsStatusCode:
    return cast(AssessmentRunNotificationSnsStatusCode, data)
