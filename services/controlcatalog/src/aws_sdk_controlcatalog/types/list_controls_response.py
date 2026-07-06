"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.controls
    import aws_sdk_controlcatalog.types.pagination_token


class ListControlsResponse(TypedDict, closed=True):
    controls: "aws_sdk_controlcatalog.types.controls.Controls"
    """<p>Returns a list of controls, given as structures of type <i>controlSummary</i>.</p>"""
    next_token: NotRequired[
        "aws_sdk_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlsResponse) -> dict:
    out: dict = {}
    import aws_sdk_controlcatalog.types.controls

    out["Controls"] = aws_sdk_controlcatalog.types.controls.serialize_json(
        value["controls"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlsResponse:
    out: ListControlsResponse = {}  # type: ignore[typeddict-item]
    if "Controls" in data:
        import aws_sdk_controlcatalog.types.controls

        out["controls"] = aws_sdk_controlcatalog.types.controls.deserialize_json(
            data["Controls"]
        )
    else:
        raise DeserializationError("ListControlsResponse.controls required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
