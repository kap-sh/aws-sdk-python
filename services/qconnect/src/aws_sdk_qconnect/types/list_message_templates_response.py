"""Generated from Smithy shape ``com.amazonaws.qconnect#ListMessageTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.message_template_summary_list
    import aws_sdk_qconnect.types.next_token


class ListMessageTemplatesResponse(TypedDict):
    message_template_summaries: "aws_sdk_qconnect.types.message_template_summary_list.MessageTemplateSummaryList"
    """<p>Summary information about the message template.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMessageTemplatesResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.message_template_summary_list

    out["messageTemplateSummaries"] = (
        aws_sdk_qconnect.types.message_template_summary_list.serialize_json(
            value["message_template_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMessageTemplatesResponse:
    out: ListMessageTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "messageTemplateSummaries" in data:
        import aws_sdk_qconnect.types.message_template_summary_list

        out["message_template_summaries"] = (
            aws_sdk_qconnect.types.message_template_summary_list.deserialize_json(
                data["messageTemplateSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListMessageTemplatesResponse.message_template_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
