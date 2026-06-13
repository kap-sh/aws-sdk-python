"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchMessageTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_search_results_list
    import aws_sdk_qconnect.types.next_token


class SearchMessageTemplatesResponse(TypedDict):
    results: "aws_sdk_qconnect.types.message_template_search_results_list.MessageTemplateSearchResultsList"
    """<p>The results of the message template search.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchMessageTemplatesResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.message_template_search_results_list

    out["results"] = (
        aws_sdk_qconnect.types.message_template_search_results_list.serialize_json(
            value["results"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchMessageTemplatesResponse:
    out: SearchMessageTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import aws_sdk_qconnect.types.message_template_search_results_list

        out["results"] = (
            aws_sdk_qconnect.types.message_template_search_results_list.deserialize_json(
                data["results"]
            )
        )
    else:
        raise DeserializationError("SearchMessageTemplatesResponse.results required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
