"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#ListApplicationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics.types.application_summaries
    import aws_sdk_kinesis_analytics.types.boolean_object


class ListApplicationsResponse(TypedDict):
    application_summaries: (
        "aws_sdk_kinesis_analytics.types.application_summaries.ApplicationSummaries"
    )
    """<p>List of <code>ApplicationSummary</code> objects. </p>"""
    has_more_applications: (
        "aws_sdk_kinesis_analytics.types.boolean_object.BooleanObject"
    )
    """<p>Returns true if there are more applications to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics.types.application_summaries

    out["ApplicationSummaries"] = (
        aws_sdk_kinesis_analytics.types.application_summaries.serialize_aws_json_1_1(
            value["application_summaries"]
        )
    )
    out["HasMoreApplications"] = value["has_more_applications"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationSummaries" in data:
        import aws_sdk_kinesis_analytics.types.application_summaries

        out["application_summaries"] = (
            aws_sdk_kinesis_analytics.types.application_summaries.deserialize_aws_json_1_1(
                data["ApplicationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListApplicationsResponse.application_summaries required"
        )
    if "HasMoreApplications" in data:
        out["has_more_applications"] = data["HasMoreApplications"]
    else:
        raise DeserializationError(
            "ListApplicationsResponse.has_more_applications required"
        )
    return out
