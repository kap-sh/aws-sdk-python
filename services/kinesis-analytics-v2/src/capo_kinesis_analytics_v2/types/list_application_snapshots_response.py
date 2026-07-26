"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ListApplicationSnapshotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.next_token
    import capo_kinesis_analytics_v2.types.snapshot_summaries


class ListApplicationSnapshotsResponse(TypedDict, closed=True):
    snapshot_summaries: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_summaries.SnapshotSummaries"
    ]
    """<p>A collection of objects containing information about the application snapshots.</p>"""
    next_token: NotRequired["capo_kinesis_analytics_v2.types.next_token.NextToken"]
    """<p>The token for the next set of results, or <code>null</code> if there are no additional results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationSnapshotsResponse) -> dict:
    out: dict = {}
    if "snapshot_summaries" in value:
        import capo_kinesis_analytics_v2.types.snapshot_summaries

        out["SnapshotSummaries"] = (
            capo_kinesis_analytics_v2.types.snapshot_summaries.serialize_aws_json_1_1(
                value["snapshot_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationSnapshotsResponse:
    out: ListApplicationSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if "SnapshotSummaries" in data:
        import capo_kinesis_analytics_v2.types.snapshot_summaries

        out["snapshot_summaries"] = (
            capo_kinesis_analytics_v2.types.snapshot_summaries.deserialize_aws_json_1_1(
                data["SnapshotSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
