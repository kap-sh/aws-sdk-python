"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RollbackApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_version_id


class RollbackApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    current_application_version_id: (
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The current application version ID. You can retrieve the application version ID using <a>DescribeApplication</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RollbackApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RollbackApplicationRequest:
    out: RollbackApplicationRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "RollbackApplicationRequest.application_name required"
        )
    if "CurrentApplicationVersionId" in data:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    else:
        raise DeserializationError(
            "RollbackApplicationRequest.current_application_version_id required"
        )
    return out
