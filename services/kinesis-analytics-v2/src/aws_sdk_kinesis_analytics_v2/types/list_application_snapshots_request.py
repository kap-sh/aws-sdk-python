"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.list_snapshots_input_limit
    import aws_sdk_kinesis_analytics_v2.types.next_token


class ListApplicationSnapshotsRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of an existing application.</p>"""
    limit: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.list_snapshots_input_limit.ListSnapshotsInputLimit"
    ]
    """<p>The maximum number of application snapshots to list.</p>"""
    next_token: NotRequired["aws_sdk_kinesis_analytics_v2.types.next_token.NextToken"]
    """<p>Use this parameter if you receive a <code>NextToken</code> response in a previous request that indicates that there is more output available. Set it to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationSnapshotsRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationSnapshotsRequest:
    out: ListApplicationSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "ListApplicationSnapshotsRequest.application_name required"
        )
    if "Limit" in data:
        out["limit"] = data["Limit"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
