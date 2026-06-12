"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.app_summary_list
    import aws_sdk_resiliencehub.types.next_token


class ListAppsResponse(TypedDict):
    app_summaries: "aws_sdk_resiliencehub.types.app_summary_list.AppSummaryList"
    """<p>Summaries for the Resilience Hub application.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.app_summary_list

    out["appSummaries"] = aws_sdk_resiliencehub.types.app_summary_list.serialize_json(
        value["app_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppsResponse:
    out: ListAppsResponse = {}  # type: ignore[typeddict-item]
    if "appSummaries" in data:
        import aws_sdk_resiliencehub.types.app_summary_list

        out["app_summaries"] = (
            aws_sdk_resiliencehub.types.app_summary_list.deserialize_json(
                data["appSummaries"]
            )
        )
    else:
        raise DeserializationError("ListAppsResponse.app_summaries required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
