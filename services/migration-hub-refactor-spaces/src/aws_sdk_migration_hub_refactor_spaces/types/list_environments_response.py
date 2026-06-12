"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListEnvironmentsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.environment_summaries
    import aws_sdk_migration_hub_refactor_spaces.types.next_token


class ListEnvironmentsResponse(TypedDict):
    environment_summary_list: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.environment_summaries.EnvironmentSummaries"
    ]
    """<p>The list of <code>EnvironmentSummary</code> objects. </p>"""
    next_token: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsResponse) -> dict:
    out: dict = {}
    if "environment_summary_list" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.environment_summaries

        out["EnvironmentSummaryList"] = (
            aws_sdk_migration_hub_refactor_spaces.types.environment_summaries.serialize_json(
                value["environment_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsResponse:
    out: ListEnvironmentsResponse = {}  # type: ignore[typeddict-item]
    if "EnvironmentSummaryList" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.environment_summaries

        out["environment_summary_list"] = (
            aws_sdk_migration_hub_refactor_spaces.types.environment_summaries.deserialize_json(
                data["EnvironmentSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
