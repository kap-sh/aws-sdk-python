"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListResourceSnapshotsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.resource_snapshot_summary_list


class ListResourceSnapshotsResponse(TypedDict, closed=True):
    resource_snapshot_summaries: "capo_partnercentral_selling.types.resource_snapshot_summary_list.ResourceSnapshotSummaryList"
    """<p> An array of resource snapshot summary objects. </p>"""
    next_token: NotRequired["str"]
    """<p> The token to retrieve the next set of results. If there are no additional results, this value is null. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceSnapshotsResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_selling.types.resource_snapshot_summary_list

    out["ResourceSnapshotSummaries"] = (
        capo_partnercentral_selling.types.resource_snapshot_summary_list.serialize_aws_json_1_0(
            value["resource_snapshot_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceSnapshotsResponse:
    out: ListResourceSnapshotsResponse = {}  # type: ignore[typeddict-item]
    if "ResourceSnapshotSummaries" in data:
        import capo_partnercentral_selling.types.resource_snapshot_summary_list

        out["resource_snapshot_summaries"] = (
            capo_partnercentral_selling.types.resource_snapshot_summary_list.deserialize_aws_json_1_0(
                data["ResourceSnapshotSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListResourceSnapshotsResponse.resource_snapshot_summaries required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
