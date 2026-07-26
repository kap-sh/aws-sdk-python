"""Generated from Smithy shape ``com.amazonaws.qconnect#ListMessageTemplateVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_version_summary_list
    import capo_qconnect.types.next_token


class ListMessageTemplateVersionsResponse(TypedDict, closed=True):
    message_template_version_summaries: "capo_qconnect.types.message_template_version_summary_list.MessageTemplateVersionSummaryList"
    """<p>Summary information about the versions of a message template.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMessageTemplateVersionsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.message_template_version_summary_list

    out["messageTemplateVersionSummaries"] = (
        capo_qconnect.types.message_template_version_summary_list.serialize_json(
            value["message_template_version_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMessageTemplateVersionsResponse:
    out: ListMessageTemplateVersionsResponse = {}  # type: ignore[typeddict-item]
    if "messageTemplateVersionSummaries" in data:
        import capo_qconnect.types.message_template_version_summary_list

        out["message_template_version_summaries"] = (
            capo_qconnect.types.message_template_version_summary_list.deserialize_json(
                data["messageTemplateVersionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListMessageTemplateVersionsResponse.message_template_version_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
