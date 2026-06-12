"""Generated from Smithy shape ``com.amazonaws.connectcases#ListTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.next_token
    import aws_sdk_connectcases.types.template_summary_list


class ListTemplatesResponse(TypedDict):
    templates: "aws_sdk_connectcases.types.template_summary_list.TemplateSummaryList"
    """<p>List of template summary objects.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesResponse) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.template_summary_list

    out["templates"] = aws_sdk_connectcases.types.template_summary_list.serialize_json(
        value["templates"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplatesResponse:
    out: ListTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "templates" in data:
        import aws_sdk_connectcases.types.template_summary_list

        out["templates"] = (
            aws_sdk_connectcases.types.template_summary_list.deserialize_json(
                data["templates"]
            )
        )
    else:
        raise DeserializationError("ListTemplatesResponse.templates required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
