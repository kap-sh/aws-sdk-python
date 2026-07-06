"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ListFormsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_summary_list


class ListFormsResponse(TypedDict, closed=True):
    entities: "aws_sdk_amplifyuibuilder.types.form_summary_list.FormSummaryList"
    """<p>The list of forms for the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFormsResponse) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.form_summary_list

    out["entities"] = aws_sdk_amplifyuibuilder.types.form_summary_list.serialize_json(
        value["entities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListFormsResponse:
    out: ListFormsResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_amplifyuibuilder.types.form_summary_list

        out["entities"] = (
            aws_sdk_amplifyuibuilder.types.form_summary_list.deserialize_json(
                data["entities"]
            )
        )
    else:
        raise DeserializationError("ListFormsResponse.entities required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
