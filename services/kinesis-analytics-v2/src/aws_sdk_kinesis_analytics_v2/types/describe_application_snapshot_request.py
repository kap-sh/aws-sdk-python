"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.snapshot_name


class DescribeApplicationSnapshotRequest(TypedDict, closed=True):
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of an existing application.</p>"""
    snapshot_name: "aws_sdk_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    """<p>The identifier of an application snapshot. You can retrieve this value using .</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationSnapshotRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    out["SnapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationSnapshotRequest:
    out: DescribeApplicationSnapshotRequest = {}  # type: ignore[typeddict-item]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError(
            "DescribeApplicationSnapshotRequest.application_name required"
        )
    if "SnapshotName" in data:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        raise DeserializationError(
            "DescribeApplicationSnapshotRequest.snapshot_name required"
        )
    return out
