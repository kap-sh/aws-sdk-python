"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppMessageTemplatesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.next_token
    import aws_sdk_socialmessaging.types.template_summary_list


class ListWhatsAppMessageTemplatesOutput(TypedDict, closed=True):
    templates: NotRequired[
        "aws_sdk_socialmessaging.types.template_summary_list.TemplateSummaryList"
    ]
    """<p>A list of template summaries.</p>"""
    next_token: NotRequired["aws_sdk_socialmessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppMessageTemplatesOutput) -> dict:
    out: dict = {}
    if "templates" in value:
        import aws_sdk_socialmessaging.types.template_summary_list

        out["templates"] = (
            aws_sdk_socialmessaging.types.template_summary_list.serialize_json(
                value["templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWhatsAppMessageTemplatesOutput:
    out: ListWhatsAppMessageTemplatesOutput = {}  # type: ignore[typeddict-item]
    if "templates" in data:
        import aws_sdk_socialmessaging.types.template_summary_list

        out["templates"] = (
            aws_sdk_socialmessaging.types.template_summary_list.deserialize_json(
                data["templates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
