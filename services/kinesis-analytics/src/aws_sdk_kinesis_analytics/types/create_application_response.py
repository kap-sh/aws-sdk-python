"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#CreateApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_summary


class CreateApplicationResponse(TypedDict, closed=True):
    application_summary: (
        "aws_sdk_kinesis_analytics.types.application_summary.ApplicationSummary"
    )
    """<p>In response to your <code>CreateApplication</code> request, Amazon Kinesis Analytics returns a response with a summary of the application it created, including the application Amazon Resource Name (ARN), name, and status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics.types.application_summary

    out["ApplicationSummary"] = (
        aws_sdk_kinesis_analytics.types.application_summary.serialize_aws_json_1_1(
            value["application_summary"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationSummary" in data:
        import aws_sdk_kinesis_analytics.types.application_summary

        out["application_summary"] = (
            aws_sdk_kinesis_analytics.types.application_summary.deserialize_aws_json_1_1(
                data["ApplicationSummary"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApplicationResponse.application_summary required"
        )
    return out
