"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ListControlsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controlcatalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controlcatalog.types.controls
    import capo_controlcatalog.types.pagination_token


class ListControlsResponse(TypedDict, closed=True):
    controls: "capo_controlcatalog.types.controls.Controls"
    """<p>Returns a list of controls, given as structures of type <i>controlSummary</i>.</p>"""
    next_token: NotRequired[
        "capo_controlcatalog.types.pagination_token.PaginationToken"
    ]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListControlsResponse) -> dict:
    out: dict = {}
    import capo_controlcatalog.types.controls

    out["Controls"] = capo_controlcatalog.types.controls.serialize_json(
        value["controls"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListControlsResponse:
    out: ListControlsResponse = {}  # type: ignore[typeddict-item]
    if "Controls" in data:
        import capo_controlcatalog.types.controls

        out["controls"] = capo_controlcatalog.types.controls.deserialize_json(
            data["Controls"]
        )
    else:
        raise DeserializationError("ListControlsResponse.controls required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
