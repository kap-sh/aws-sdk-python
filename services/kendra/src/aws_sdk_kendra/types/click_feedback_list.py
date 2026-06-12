"""Generated from Smithy shape ``com.amazonaws.kendra#ClickFeedbackList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kendra.types.click_feedback

ClickFeedbackList: TypeAlias = list["aws_sdk_kendra.types.click_feedback.ClickFeedback"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClickFeedbackList) -> list:
    import aws_sdk_kendra.types.click_feedback

    out: list = []
    for item in value:
        out.append(aws_sdk_kendra.types.click_feedback.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClickFeedbackList:
    import aws_sdk_kendra.types.click_feedback

    out: ClickFeedbackList = []
    for item in data:
        out.append(aws_sdk_kendra.types.click_feedback.deserialize_aws_json_1_1(item))
    return out
