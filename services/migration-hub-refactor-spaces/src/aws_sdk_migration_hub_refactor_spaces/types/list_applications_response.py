"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListApplicationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.application_summaries
    import aws_sdk_migration_hub_refactor_spaces.types.next_token


class ListApplicationsResponse(TypedDict):
    application_summary_list: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.application_summaries.ApplicationSummaries"
    ]
    """<p>The list of <code>ApplicationSummary</code> objects. </p>"""
    next_token: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    if "application_summary_list" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.application_summaries

        out["ApplicationSummaryList"] = (
            aws_sdk_migration_hub_refactor_spaces.types.application_summaries.serialize_json(
                value["application_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "ApplicationSummaryList" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.application_summaries

        out["application_summary_list"] = (
            aws_sdk_migration_hub_refactor_spaces.types.application_summaries.deserialize_json(
                data["ApplicationSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
