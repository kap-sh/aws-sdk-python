"""Generated from Smithy shape ``com.amazonaws.evs#ListEnvironmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_evs.types.environment_summary_list
    import aws_sdk_evs.types.pagination_token


class ListEnvironmentsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_evs.types.pagination_token.PaginationToken"]
    """<p>A unique pagination token for next page results. Make the call again using this token to retrieve the next page.</p>"""
    environment_summaries: NotRequired[
        "aws_sdk_evs.types.environment_summary_list.EnvironmentSummaryList"
    ]
    """<p>A list of environments with summarized environment details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "environment_summaries" in value:
        import aws_sdk_evs.types.environment_summary_list

        out["environmentSummaries"] = (
            aws_sdk_evs.types.environment_summary_list.serialize_aws_json_1_0(
                value["environment_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentsResponse:
    out: ListEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "environmentSummaries" in data:
        import aws_sdk_evs.types.environment_summary_list

        out["environment_summaries"] = (
            aws_sdk_evs.types.environment_summary_list.deserialize_aws_json_1_0(
                data["environmentSummaries"]
            )
        )
    return out
