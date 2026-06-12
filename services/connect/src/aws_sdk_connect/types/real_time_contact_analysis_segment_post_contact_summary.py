"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentPostContactSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_content
    import aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_failure_code
    import aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_status


class RealTimeContactAnalysisSegmentPostContactSummary(TypedDict):
    content: NotRequired[
        "aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_content.RealTimeContactAnalysisPostContactSummaryContent"
    ]
    """<p>The content of the summary.</p>"""
    status: "aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_status.RealTimeContactAnalysisPostContactSummaryStatus"
    """<p>Whether the summary was successfully COMPLETED or FAILED to be generated.</p>"""
    failure_code: NotRequired[
        "aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_failure_code.RealTimeContactAnalysisPostContactSummaryFailureCode"
    ]
    """<p>If the summary failed to be generated, one of the following failure codes occurs:</p> <ul> <li> <p> <code>QUOTA_EXCEEDED</code>: The number of concurrent analytics jobs reached your service quota.</p> </li> <li> <p> <code>INSUFFICIENT_CONVERSATION_CONTENT</code>: The conversation needs to have at least one turn from both the participants in order to generate the summary.</p> </li> <li> <p> <code>FAILED_SAFETY_GUIDELINES</code>: The generated summary cannot be provided because it failed to meet system safety guidelines.</p> </li> <li> <p> <code>INVALID_ANALYSIS_CONFIGURATION</code>: This code occurs when, for example, you're using a <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/supported-languages.html#supported-languages-contact-lens\">language</a> that isn't supported by generative AI-powered post-contact summaries. </p> </li> <li> <p> <code>INTERNAL_ERROR</code>: Internal system error.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentPostContactSummary) -> dict:
    out: dict = {}
    if "content" in value:
        out["Content"] = value["content"]
    import aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_status

    out["Status"] = (
        aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_status.serialize_json(
            value["status"]
        )
    )
    if "failure_code" in value:
        import aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_failure_code

        out["FailureCode"] = (
            aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_failure_code.serialize_json(
                value["failure_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentPostContactSummary:
    out: RealTimeContactAnalysisSegmentPostContactSummary = {}  # type: ignore[typeddict-item]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Status" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_status

        out["status"] = (
            aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        raise DeserializationError(
            "RealTimeContactAnalysisSegmentPostContactSummary.status required"
        )
    if "FailureCode" in data:
        import aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_failure_code

        out["failure_code"] = (
            aws_sdk_connect.types.real_time_contact_analysis_post_contact_summary_failure_code.deserialize_json(
                data["FailureCode"]
            )
        )
    return out
