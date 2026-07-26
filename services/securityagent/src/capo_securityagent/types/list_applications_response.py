"""Generated from Smithy shape ``com.amazonaws.securityagent#ListApplicationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.application_summary_list
    import capo_securityagent.types.next_token


class ListApplicationsResponse(TypedDict, closed=True):
    application_summaries: (
        "capo_securityagent.types.application_summary_list.ApplicationSummaryList"
    )
    """<p>The list of application summaries.</p>"""
    next_token: NotRequired["capo_securityagent.types.next_token.NextToken"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request. For subsequent calls, use the nextToken value returned from the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListApplicationsResponse) -> dict:
    out: dict = {}
    import capo_securityagent.types.application_summary_list

    out["applicationSummaries"] = (
        capo_securityagent.types.application_summary_list.serialize_json(
            value["application_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListApplicationsResponse:
    out: ListApplicationsResponse = {}  # type: ignore[typeddict-item]
    if "applicationSummaries" in data:
        import capo_securityagent.types.application_summary_list

        out["application_summaries"] = (
            capo_securityagent.types.application_summary_list.deserialize_json(
                data["applicationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListApplicationsResponse.application_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
