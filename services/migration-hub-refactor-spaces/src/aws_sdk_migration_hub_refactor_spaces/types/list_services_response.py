"""Generated from Smithy shape ``com.amazonaws.migrationhubrefactorspaces#ListServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migration_hub_refactor_spaces.types.next_token
    import aws_sdk_migration_hub_refactor_spaces.types.service_summaries


class ListServicesResponse(TypedDict, closed=True):
    service_summary_list: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.service_summaries.ServiceSummaries"
    ]
    """<p> The list of <code>ServiceSummary</code> objects. </p>"""
    next_token: NotRequired[
        "aws_sdk_migration_hub_refactor_spaces.types.next_token.NextToken"
    ]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicesResponse) -> dict:
    out: dict = {}
    if "service_summary_list" in value:
        import aws_sdk_migration_hub_refactor_spaces.types.service_summaries

        out["ServiceSummaryList"] = (
            aws_sdk_migration_hub_refactor_spaces.types.service_summaries.serialize_json(
                value["service_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServicesResponse:
    out: ListServicesResponse = {}  # type: ignore[typeddict-item]
    if "ServiceSummaryList" in data:
        import aws_sdk_migration_hub_refactor_spaces.types.service_summaries

        out["service_summary_list"] = (
            aws_sdk_migration_hub_refactor_spaces.types.service_summaries.deserialize_json(
                data["ServiceSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
