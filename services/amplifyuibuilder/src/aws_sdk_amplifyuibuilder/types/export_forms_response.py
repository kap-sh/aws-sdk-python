"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ExportFormsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_amplifyuibuilder.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.form_list


class ExportFormsResponse(TypedDict):
    entities: "aws_sdk_amplifyuibuilder.types.form_list.FormList"
    """<p>Represents the configuration of the exported forms.</p>"""
    next_token: NotRequired["str"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportFormsResponse) -> dict:
    out: dict = {}
    import aws_sdk_amplifyuibuilder.types.form_list

    out["entities"] = aws_sdk_amplifyuibuilder.types.form_list.serialize_json(
        value["entities"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ExportFormsResponse:
    out: ExportFormsResponse = {}  # type: ignore[typeddict-item]
    if "entities" in data:
        import aws_sdk_amplifyuibuilder.types.form_list

        out["entities"] = aws_sdk_amplifyuibuilder.types.form_list.deserialize_json(
            data["entities"]
        )
    else:
        raise DeserializationError("ExportFormsResponse.entities required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
