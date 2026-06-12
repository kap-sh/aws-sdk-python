"""Generated from Smithy shape ``com.amazonaws.applicationinsights#DescribeProblemResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_application_insights.types.problem
    import aws_sdk_application_insights.types.sns_notification_arn


class DescribeProblemResponse(TypedDict):
    problem: NotRequired["aws_sdk_application_insights.types.problem.Problem"]
    """<p>Information about the problem. </p>"""
    sns_notification_arn: NotRequired[
        "aws_sdk_application_insights.types.sns_notification_arn.SNSNotificationArn"
    ]
    """<p> The SNS notification topic ARN of the problem. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProblemResponse) -> dict:
    out: dict = {}
    if "problem" in value:
        import aws_sdk_application_insights.types.problem

        out["Problem"] = (
            aws_sdk_application_insights.types.problem.serialize_aws_json_1_1(
                value["problem"]
            )
        )
    if "sns_notification_arn" in value:
        out["SNSNotificationArn"] = value["sns_notification_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProblemResponse:
    out: DescribeProblemResponse = {}  # type: ignore[typeddict-item]
    if "Problem" in data:
        import aws_sdk_application_insights.types.problem

        out["problem"] = (
            aws_sdk_application_insights.types.problem.deserialize_aws_json_1_1(
                data["Problem"]
            )
        )
    if "SNSNotificationArn" in data:
        out["sns_notification_arn"] = data["SNSNotificationArn"]
    return out
