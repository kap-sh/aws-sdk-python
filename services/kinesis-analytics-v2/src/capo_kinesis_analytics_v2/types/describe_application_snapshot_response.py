"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#DescribeApplicationSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_details


class DescribeApplicationSnapshotResponse(TypedDict, closed=True):
    snapshot_details: "capo_kinesis_analytics_v2.types.snapshot_details.SnapshotDetails"
    """<p>An object containing information about the application snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationSnapshotResponse) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.snapshot_details

    out["SnapshotDetails"] = (
        capo_kinesis_analytics_v2.types.snapshot_details.serialize_aws_json_1_1(
            value["snapshot_details"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationSnapshotResponse:
    out: DescribeApplicationSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "SnapshotDetails" in data:
        import capo_kinesis_analytics_v2.types.snapshot_details

        out["snapshot_details"] = (
            capo_kinesis_analytics_v2.types.snapshot_details.deserialize_aws_json_1_1(
                data["SnapshotDetails"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeApplicationSnapshotResponse.snapshot_details required"
        )
    return out
