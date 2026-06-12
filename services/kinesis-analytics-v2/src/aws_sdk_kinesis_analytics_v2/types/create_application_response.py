"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#CreateApplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_detail


class CreateApplicationResponse(TypedDict):
    application_detail: (
        "aws_sdk_kinesis_analytics_v2.types.application_detail.ApplicationDetail"
    )
    """<p>In response to your <code>CreateApplication</code> request, Managed Service for Apache Flink returns a response with details of the application it created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApplicationResponse) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.application_detail

    out["ApplicationDetail"] = (
        aws_sdk_kinesis_analytics_v2.types.application_detail.serialize_aws_json_1_1(
            value["application_detail"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApplicationResponse:
    out: CreateApplicationResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationDetail" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_detail

        out["application_detail"] = (
            aws_sdk_kinesis_analytics_v2.types.application_detail.deserialize_aws_json_1_1(
                data["ApplicationDetail"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApplicationResponse.application_detail required"
        )
    return out
