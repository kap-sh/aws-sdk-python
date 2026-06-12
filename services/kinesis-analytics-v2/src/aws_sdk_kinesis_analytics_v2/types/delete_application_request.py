"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.timestamp


class DeleteApplicationRequest(TypedDict):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of the application to delete.</p>"""
    create_timestamp: "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    """<p>Use the <code>DescribeApplication</code> operation to get this value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    import aws_sdk_kinesis_analytics_v2.types.timestamp

    out["CreateTimestamp"] = (
        aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
            value["create_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationRequest:
    out: DeleteApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("DeleteApplicationRequest.application_name required")
    if "CreateTimestamp" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["create_timestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    else:
        raise DeserializationError("DeleteApplicationRequest.create_timestamp required")
    return out
