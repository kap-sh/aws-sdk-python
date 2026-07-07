"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DeleteApplicationReferenceDataSourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.id


class DeleteApplicationReferenceDataSourceRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of an existing application.</p>"""
    current_application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The current application version. You can use the <a>DescribeApplication</a> operation to get the current application version. If the version specified is not the current version, the <code>ConcurrentModificationException</code> is returned.</p>"""
    reference_id: "aws_sdk_kinesis_analytics_v2.types.id.Id"
    """<p>The ID of the reference data source. When you add a reference data source to your application using the <a>AddApplicationReferenceDataSource</a>, Kinesis Data Analytics assigns an ID. You can use the <a>DescribeApplication</a> operation to get the reference ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteApplicationReferenceDataSourceRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    out["ReferenceId"] = value["reference_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteApplicationReferenceDataSourceRequest:
    out: DeleteApplicationReferenceDataSourceRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DeleteApplicationReferenceDataSourceRequest.application_name required"
        )
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "DeleteApplicationReferenceDataSourceRequest.current_application_version_id required"
        )
    if "ReferenceId" in data:
        out["reference_id"] = data["ReferenceId"]
    else:
        raise DeserializationError(
            "DeleteApplicationReferenceDataSourceRequest.reference_id required"
        )
    return out
