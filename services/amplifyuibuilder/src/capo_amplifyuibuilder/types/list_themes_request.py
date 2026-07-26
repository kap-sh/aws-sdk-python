"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ListThemesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.list_entity_limit


class ListThemesRequest(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the Amplify app.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is a part of the Amplify app.</p>"""
    next_token: NotRequired["str"]
    """<p>The token to request the next page of results.</p>"""
    max_results: NotRequired[
        "capo_amplifyuibuilder.types.list_entity_limit.ListEntityLimit"
    ]
    """<p>The maximum number of theme results to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListThemesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListThemesRequest:
    out: ListThemesRequest = {}  # type: ignore[typeddict-item]
    return out
