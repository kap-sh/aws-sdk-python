"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SearchSystemInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.next_token
    import capo_iotthingsgraph.types.system_instance_summaries


class SearchSystemInstancesResponse(TypedDict, closed=True):
    summaries: NotRequired[
        "capo_iotthingsgraph.types.system_instance_summaries.SystemInstanceSummaries"
    ]
    """<p>An array of objects that contain summary data abour the system instances in the result set.</p>"""
    next_token: NotRequired["capo_iotthingsgraph.types.next_token.NextToken"]
    """<p>The string to specify as <code>nextToken</code> when you request the next page of results. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchSystemInstancesResponse) -> dict:
    out: dict = {}
    if "summaries" in value:
        import capo_iotthingsgraph.types.system_instance_summaries

        out["summaries"] = (
            capo_iotthingsgraph.types.system_instance_summaries.serialize_aws_json_1_1(
                value["summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchSystemInstancesResponse:
    out: SearchSystemInstancesResponse = {}  # type: ignore[typeddict-item]
    if "summaries" in data:
        import capo_iotthingsgraph.types.system_instance_summaries

        out["summaries"] = (
            capo_iotthingsgraph.types.system_instance_summaries.deserialize_aws_json_1_1(
                data["summaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
