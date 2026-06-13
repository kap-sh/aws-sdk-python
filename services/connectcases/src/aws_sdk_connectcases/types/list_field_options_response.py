"""Generated from Smithy shape ``com.amazonaws.connectcases#ListFieldOptionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_options_list
    import aws_sdk_connectcases.types.next_token


class ListFieldOptionsResponse(TypedDict):
    options: "aws_sdk_connectcases.types.field_options_list.FieldOptionsList"
    """<p>A list of <code>FieldOption</code> objects.</p>"""
    next_token: NotRequired["aws_sdk_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFieldOptionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_connectcases.types.field_options_list

    out["options"] = aws_sdk_connectcases.types.field_options_list.serialize_json(
        value["options"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFieldOptionsResponse:
    out: ListFieldOptionsResponse = {}  # type: ignore[typeddict-item]
    if "options" in data:
        import aws_sdk_connectcases.types.field_options_list

        out["options"] = aws_sdk_connectcases.types.field_options_list.deserialize_json(
            data["options"]
        )
    else:
        raise DeserializationError("ListFieldOptionsResponse.options required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
